from scholarly import scholarly
import jsonpickle
import json
import logging
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
if not scholar_id:
    raise SystemExit('Set the GOOGLE_SCHOLAR_ID repository secret before running the crawler.')

scholarly.set_timeout(20)
scholarly.set_retries(3)
logging.info('Fetching Google Scholar profile and citation data')
author: dict = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
