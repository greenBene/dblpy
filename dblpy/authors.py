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

    def __init__(self, name:str, url:str, notes:dict = None) -> None:
        self.name = name
        self.url = url

        if notes:
            self._prepare_notes(notes)

    def __str__(self) -> str:
        s = self.name
        s += f' ({self.url})'
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


def get_authors(q: str) -> List[Author]:
    authors_dict = DblpAPI.load_hits(endpoint='author', q=q)
    authors_objects = [
        Author(
            author['info']['author'], 
            author['info']['url'], 
            author['info']['notes']['note'] 
                if 'notes' in author['info'] else None)
        for author in authors_dict]

    return authors_objects


if __name__ == '__main__':
    print(DblpAPI.load_hits('author', 'Donald Kn'))


    # authors = get_authors(q='Donald E. Knuth')
    # for a in authors:
    #     print(a)