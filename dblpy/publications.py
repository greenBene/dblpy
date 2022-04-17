from typing import List
from dblpy import authors
from dblpy.dblp_api import DblpAPI

class Publication():
    """Class to wrap publication results of dblp search api"""

    authors: List[str] = [] # List of author names 
    title: str = '' # Name of publication
    venue: str = '' # Venue of publication
    volume: str = '' # Volume in which publication was published
    number: str = '' # Number of publication volume
    pages: str = '' # Pages of publication 
    publisher: str = '' # Publisher of publication
    year: str = '' # Year when publication was published
    type: str = '' # Type of publication
    access: str = '' # Type of access
    key: str = '' # Key of publication
    doi: str = '' # doi of publication 
    ee: str = '' # Link to electronic edition of publication
    url: str = '' # Link to dblp page of publication

    def __init__(self, authors:List, title: str, venue: str, volume :str, number: str, pages: str, publisher: str, year: str, type: str, access: str, key: str, doi: str, ee: str, url: str) -> None:
        self.title = title
        self.venue = venue
        self.volume = volume
        self.number = number
        self.pages = pages
        self.publisher = publisher
        self.year = year
        self.type = type
        self.access = access
        self.key = key
        self.doi = doi
        self.ee = ee
        self.url = url
        self.authors = self._prepare_authors(authors)
    
    def _prepare_authors(self, authors):
        if authors == None:
            return ['']
        if type(authors) != list:
            authors = [authors]
        return [author['text'] for author in authors]

    def __str__(self) -> str:
        s = f'{self.year}. {self.authors[0] if self.authors != None else ""} et al. "{self.title}". ({self.url})'
        return s


def get_publications(q: str, max_results: int = 100) -> List[Publication]:
    """
    Get a list of publications matching the query q.

    Keyword arguments:
    q:str -- query to search for publications
    max_results:int -- maximum number of authors to return (default 100)
    """
    publications_dict = DblpAPI.load_hits(endpoint='publ', q=q, max_results=max_results)

    publications_objects = [
        Publication(
            authors=publication['info']['authors']['author']
                if 'authors' in publication['info'] else None,
            title=publication['info']['title'],
            venue=publication['info'].get('venue', ''),
            volume=publication['info'].get('volume', ''),
            number=publication['info'].get('number', ''),
            pages=publication['info'].get('pages', ''),
            publisher=publication['info'].get('publisher', ''),
            year=publication['info'].get('year', ''),
            type=publication['info'].get('type', ''),
            access=publication['info'].get('access', ''),
            key=publication['info'].get('key', ''),
            doi=publication['info'].get('doi', ''),
            ee=publication['info'].get('ee', ''),
            url=publication['info'].get('url', '')
        )
        for publication in publications_dict
    ]

    return publications_objects


if __name__ == '__main__':
    publ = get_publications(q='knuth', max_results=500)
    for p in publ:
        print(p)