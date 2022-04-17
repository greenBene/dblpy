from typing import List

from dblpy.dblp_api import DblpAPI

class AuthorNote():
    """Class to wrap notes of authors from results of dblp search api"""
    
    type:str = ''
    text:str = ''

    def __init__(self, type:str, text:str) -> None:
        self.type = type # Type of affiliation
        self.text = text # Name of affiliation

    def __str__(self) -> str:
        s = f'{self.type}: {self.text}'
        return s

class Author():
    """Class to wrap author results of dblp search api"""

    name:str = '' # Name of Author
    notes:List[AuthorNote] = [] # List of affiliations and awards linked to author
    url:str = '' # Link to dblp page of author
    aliases:List[str] = [] # List of other names of same author

    def __init__(self, name:str, url:str, notes = None, aliases:dict = None) -> None:
        self.name = name
        self.url = url
        if notes:
            self._prepare_notes(notes)
        if aliases:
            self._prepare_aliases(aliases)

    def __str__(self) -> str:
        s = f'{self.name} ({self.url})'
        return s

    def _prepare_notes(self, notes):
        if type(notes) == dict:
            notes = [notes]
        self.notes = [
            AuthorNote(
                type=note['@type'], 
                text=note['text']) 
            for note in notes]
        return notes

    def _prepare_aliases(self, aliases):
        if type(aliases) != list:
            aliases = [aliases]

        self.aliases = [
            alias
            for alias in aliases]
        return aliases


def get_authors(q: str, max_results: int = 100) -> List[Author]:
    """
    Get a list of authors matching the query q.

    Keyword arguments:
    q:str -- query to search for author
    max_results:int -- maximum number of authors to return (default 100)
    """
    authors_dict = DblpAPI.load_hits(endpoint='author', q=q, max_results=max_results)
    authors_objects = [
        Author(
            name=author['info']['author'], 
            url=author['info']['url'], 
            notes=author['info']['notes']['note'] 
                if 'notes' in author['info'] else None,
            aliases=author['info']['aliases']['alias']
                if 'aliases' in author['info'] else None)
        for author in authors_dict]

    return authors_objects


if __name__ == '__main__':
    publ = get_authors(q='Donald Ervin Knuth')
    for p in publ:
        print(p)