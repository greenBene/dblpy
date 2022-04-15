from typing import List

from dblpy.dblp_api import DblpAPI

class AuthorNote():
    type:str = ''
    text:str = ''

    def __init__(self, type:str, text:str) -> None:
        self.type = type
        self.text = text

    def __str__(self) -> str:
        s = f'{self.type}: {self.text}'
        return s

class Author():
    name:str = ''
    notes:List[AuthorNote] = []
    url:str = ''
    aliases:List[str] = []

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
    publ = get_authors(q='Knuth')
    for p in publ:
        print(p)