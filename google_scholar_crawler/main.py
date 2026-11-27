from datetime import UTC, datetime
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def parse_profile(html, scholar_id):
    profile = BeautifulSoup(html, "html.parser")
    name = profile.select_one("#gsc_prf_in")
    metrics = profile.select("#gsc_rsb_st td.gsc_rsb_std")
    if name is None or len(metrics) != 6:
        raise ValueError("Google Scholar did not return a public profile with citation metrics.")

    more_papers = profile.select_one("#gsc_bpf_more")
    if more_papers is not None and not more_papers.has_attr("disabled"):
        raise ValueError("The public profile page does not contain the full publication list.")

    publications = {}
    for row in profile.select("#gsc_a_b .gsc_a_tr"):
        title = row.select_one("a.gsc_a_at[href]")
        citation_cell = row.select_one(".gsc_a_c")
        if title is None or citation_cell is None:
            raise ValueError("Google Scholar returned an incomplete publication row.")

        publication_ids = parse_qs(urlsplit(title["href"]).query).get("citation_for_view", [])
        if len(publication_ids) != 1 or not publication_ids[0].startswith(f"{scholar_id}:"):
            raise ValueError("Google Scholar returned an unexpected publication ID.")
        publication_id = publication_ids[0]
        year = row.select_one(".gsc_a_y")
        citations = citation_cell.select_one(".gsc_a_ac")
        publications[publication_id] = {
            "author_pub_id": publication_id,
            "bib": {"title": title.get_text(strip=True), "pub_year": year.get_text(strip=True) if year else ""},
            "num_citations": int(citations.get_text(strip=True) or "0") if citations else 0,
        }

    metric_names = ("citedby", "citedby5y", "hindex", "hindex5y", "i10index", "i10index5y")
    author = {key: int(cell.get_text(strip=True)) for key, cell in zip(metric_names, metrics)}
    if author["citedby"] and not publications:
        raise ValueError("Google Scholar did not return any publication rows for this profile.")

    return {
        **author,
        "scholar_id": scholar_id,
        "name": name.get_text(strip=True),
        "updated": datetime.now(UTC).isoformat(),
        "publications": publications,
    }


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise SystemExit("Set the GOOGLE_SCHOLAR_ID repository secret before running the crawler.")

    # Google Scholar's robots.txt allows public profile URLs starting with ?user=.
    query = urlencode({"user": scholar_id, "hl": "en", "pagesize": 100})
    url = f"https://scholar.google.com/citations?{query}"
    request = Request(url, headers={"User-Agent": "CitationStats/1.0"})
    try:
        with urlopen(request, timeout=20) as response:
            if response.geturl() != url:
                raise ValueError("Google Scholar redirected away from the public profile.")
            author = parse_profile(response.read(), scholar_id)
    except HTTPError as error:
        raise SystemExit(f"Google Scholar returned HTTP {error.code}. Keeping the last published data.") from error
    except (URLError, TimeoutError, ValueError) as error:
        raise SystemExit(f"{error} Keeping the last published data.") from error

    results = Path("results")
    results.mkdir(exist_ok=True)
    badge = {"schemaVersion": 1, "label": "citations", "message": str(author["citedby"])}
    (results / "gs_data.json").write_text(json.dumps(author, ensure_ascii=False), encoding="utf-8")
    (results / "gs_data_shieldsio.json").write_text(json.dumps(badge), encoding="utf-8")
    print(f"Fetched {author['citedby']} citations and {len(author['publications'])} publications.")


if __name__ == "__main__":
    main()
