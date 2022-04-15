

from dblpy.dblp_api import DblpAPI


class Venue():
    venue: str = ''
    acronym: str = ''
    type: str = ''
    url: str = ''

    def __init__(self, venue: str, acronym: str, type: str, url: str) -> None:
        self.venue = venue
        self.acronym = acronym
        self.type = type
        self.url = url

    def __str__(self) -> str:
        s = f'{self.venue} ({self.url})'
        return s

def get_venues(q: str, max_results: int = 100):
    venue_dict = DblpAPI.load_hits('venue', q=q, max_results=max_results)

    venue_objects = [
        Venue(
            venue=venue['info'].get('venue', ''),
            acronym=venue['info'].get('acronym', ''),
            type=venue['info'].get('type', ''),
            url=venue['info'].get('url', '')
        )
        for venue in venue_dict
    ]

    return venue_objects

if __name__ == "__main__":
    venues = get_venues(q='Berlin')
    for v in venues:
        print(v)
