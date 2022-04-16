import requests
import urllib.parse

class DblpAPI():

    BASE_URL = 'https://dblp.org/search/{endpoint}/api?'

    @staticmethod
    def load_hits(endpoint: str, q: str, max_results: int = 100):
        hits = []
        total = -1
        first_id = 0

        while len(hits) != total and len(hits) < max_results:
            params = {
                'q': q,
                'format': 'json',
                'h': 50,
                'f': first_id
            }
            url = DblpAPI.BASE_URL.format(endpoint=endpoint) + urllib.parse.urlencode(params)
            re = requests.get(url=url)

            if not re.ok:
                raise DblpApiError(f'Could not load data from DBLP API. Status code: {re.status_code}. Error code: {re.json().get("status", "")}' )

            result = re.json()['result']

            total = int(result['hits']['@total'])
            sent = int(result['hits']['@sent'])
            if sent > 0:
                hits += result['hits']['hit']

            first_id = len(hits)

        return hits[:max_results]

class DblpApiError(Exception):
    pass