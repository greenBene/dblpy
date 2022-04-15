import unittest
from unittest.mock import Mock
from dblpy import Author, DblpAPI, get_authors

class AuthorsTestCase(unittest.TestCase):

    def test_create_author(self):
        author = Author(
            name='Donald E. Knuth',
            url='https://dblp.org/pid/k/DonaldEKnuth',
            notes=[
                {
                    "@type":"affiliation",
                    "text":"Stanford University, Com…nce Department, CA, USA"},
                {
                    "@type":"award",
                    "text":"Turing Award"},
                {
                    "@type":"award",
                    "text":"BBVA Foundation Frontiers of Knowledge Award"}
            ],
            aliases=['Donald Ervin Knuth']
        )
        self.assertEqual(author.name, 'Donald E. Knuth')
        self.assertEqual(author.url, 'https://dblp.org/pid/k/DonaldEKnuth')
        self.assertEqual(author.notes[0].type, 'affiliation')
        self.assertEqual(author.notes[0].text, 'Stanford University, Com…nce Department, CA, USA')
        self.assertEqual(author.notes[1].type, 'award')
        self.assertEqual(author.notes[1].text, 'Turing Award')
        self.assertEqual(author.notes[2].type, 'award')
        self.assertEqual(author.notes[2].text, 'BBVA Foundation Frontiers of Knowledge Award')
        self.assertEqual(author.aliases, ['Donald Ervin Knuth'])

    def test_print_author(self):
        author = Author(
            name='Donald E. Knuth',
            url='https://dblp.org/pid/k/DonaldEKnuth',
            notes=[
                {
                    "@type":"affiliation",
                    "text":"Stanford University, Com…nce Department, CA, USA"},
                {
                    "@type":"award",
                    "text":"Turing Award"},
                {
                    "@type":"award",
                    "text":"BBVA Foundation Frontiers of Knowledge Award"}
            ],
            aliases=['Donald Ervin Knuth']
        )

        self.assertEqual(str(author), 'Donald E. Knuth (https://dblp.org/pid/k/DonaldEKnuth)')


    def test_get_authors(self):
        DblpAPI.load_hits = Mock(
            return_value=[
                {
                    'info': {
                        'author': 'Donald E. Knuth', 
                        'aliases': {'alias': 'Donald Ervin Knuth'}, 
                        'notes': {'note': [
                            {'@type': 'affiliation', 'text': 'Stanford University, Computer Science Department, CA, USA'}, 
                            {'@type': 'award', 'text': 'Turing Award'}, 
                            {'@type': 'award', 'text': 'BBVA Foundation Frontiers of Knowledge Award'}]}, 
                        'url': 'https://dblp.org/pid/k/DonaldEKnuth'}}, 
                {
                    'info': {
                        'author': 'Donald O. Knight', 
                        'url': 'https://dblp.org/pid/32/2048'}}, 
                {
                    'info': 
                        {'author': 'Don Knox', 
                        'aliases': {'alias': 'Donald Knox'}, 
                        'notes': {'note': {
                            '@type': 'affiliation', 
                            'text': 'Glasgow Caledonian University, UK'}}, 
                        'url': 'https://dblp.org/pid/121/6484'}}])
        
        authors = get_authors(q='Donal Kn')

        self.assertEqual(authors[0].name, 'Donald E. Knuth')
        self.assertEqual(authors[1].name, 'Donald O. Knight')
        self.assertEqual(authors[2].name, 'Don Knox')
