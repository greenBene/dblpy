

from dblpy.dblp_api import DblpAPI


class Venue():
    """Class to wrap venue results of dblp search api"""
    
    venue: str = '' # Name of venue
    acronym: str = '' # Acronym of venue
    type: str = '' # Type of venue
    url: str = '' # Link to dblp page of venue

    def __init__(self, name: str, acronym: str, type: str, url: str) -> None:
        self.name = name
        self.acronym = acronym
        self.type = type
        self.url = url

    def __str__(self) -> str:
        s = f'{self.name} ({self.url})'
        return s

def get_venues(q: str, max_results: int = 100):
    """
    Get a list of venues matching the query q.

    Keyword arguments:
    q:str -- query to search for venues
    max_results:int -- maximum number of authors to return (default 100)
    """
    venue_dict = DblpAPI.load_hits('venue', q=q, max_results=max_results)

    venue_objects = [
        Venue(
            name=venue['info'].get('venue', ''),
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
