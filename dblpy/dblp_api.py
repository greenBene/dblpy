import requests
import urllib.parse

class DblpAPI():

    BASE_URL = 'https://dblp.org/search/{endpoint}/api?'

    @staticmethod
    def load_hits(endpoint: str, q: str):
        hits = []
        total = -1
        first_id = 0

        while total != len(hits):
            params = {
                'q': q,
                'format': 'json',
                'h': 10,
                'f': first_id
            }
            url = DblpAPI.BASE_URL.format(endpoint=endpoint) + urllib.parse.urlencode(params)
            re = requests.get(url=url)
            result = re.json()['result']

            total = int(result['hits']['@total'])
            sent = int(result['hits']['@sent'])
            if sent > 0:
                hits += result['hits']['hit']

            first_id = len(hits)

        return hits