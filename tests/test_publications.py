import unittest
from dblpy import Publication, get_publications
from dblpy.dblp_api import DblpAPI
from unittest.mock import Mock

class PublicationsTestCase(unittest.TestCase):
    def test_create_publication(self):
        publication = Publication(
            authors=[
                {"@pid":"p/CHPapadimitriou","text":"Christos H. Papadimitriou"},
                {"@pid":"a/LeonardMAdleman","text":"Leonard M. Adleman"},
                {"@pid":"k/RichardMKarp","text":"Richard M. Karp"},
                {"@pid":"k/DonaldEKnuth","text":"Donald E. Knuth"},
                {"@pid":"t/RobertEndreTarjan","text":"Robert E. Tarjan"},
                {"@pid":"v/LeslieGValiant","text":"Leslie G. Valiant"}
            ],
            title='An Algorithmic View of the Universe',
            venue='ACM-TURING',
            volume='',
            number='',
            pages='I-XIII, 1-441',
            publisher='',
            year='2012',
            type='Conference and Workshop Papers',
            access='closed',
            key='conf/acm/PapadimitriouAK12',
            doi='10.1145/2322176.2322189',
            ee='https://doi.org/10.1145/2322176.2322189',
            url='https://dblp.org/rec/conf/acm/PapadimitriouAK12')
        
        self.assertEqual(publication.authors[0], 'Christos H. Papadimitriou')
        self.assertEqual(publication.authors[1], 'Leonard M. Adleman')
        self.assertEqual(publication.authors[2], 'Richard M. Karp')
        self.assertEqual(publication.authors[3], 'Donald E. Knuth')
        self.assertEqual(publication.authors[4], 'Robert E. Tarjan')
        self.assertEqual(publication.authors[5], 'Leslie G. Valiant')
        self.assertEqual(publication.title, 'An Algorithmic View of the Universe')
        self.assertEqual(publication.venue, 'ACM-TURING')
        self.assertEqual(publication.pages, 'I-XIII, 1-441')
        self.assertEqual(publication.year, '2012')
        self.assertEqual(publication.type, 'Conference and Workshop Papers')
        self.assertEqual(publication.access, 'closed')
        self.assertEqual(publication.key, 'conf/acm/PapadimitriouAK12')
        self.assertEqual(publication.doi, '10.1145/2322176.2322189')
        self.assertEqual(publication.ee, 'https://doi.org/10.1145/2322176.2322189')
        self.assertEqual(publication.url, 'https://dblp.org/rec/conf/acm/PapadimitriouAK12')
    
    def test_print_publication(self):
        publication = Publication(
            authors=[
                {"@pid":"p/CHPapadimitriou","text":"Christos H. Papadimitriou"},
                {"@pid":"a/LeonardMAdleman","text":"Leonard M. Adleman"},
                {"@pid":"k/RichardMKarp","text":"Richard M. Karp"},
                {"@pid":"k/DonaldEKnuth","text":"Donald E. Knuth"},
                {"@pid":"t/RobertEndreTarjan","text":"Robert E. Tarjan"},
                {"@pid":"v/LeslieGValiant","text":"Leslie G. Valiant"}
            ],
            title='An Algorithmic View of the Universe',
            venue='ACM-TURING',
            volume='',
            number='',
            pages='I-XIII, 1-441',
            publisher='',
            year='2012',
            type='Conference and Workshop Papers',
            access='closed',
            key='conf/acm/PapadimitriouAK12',
            doi='10.1145/2322176.2322189',
            ee='https://doi.org/10.1145/2322176.2322189',
            url='https://dblp.org/rec/conf/acm/PapadimitriouAK12')
        
        self.assertEqual(str(publication), '2012. Christos H. Papadimitriou et al. "An Algorithmic View of the Universe". (https://doi.org/10.1145/2322176.2322189)')
    
    def test_get_publications(self):
        DblpAPI.load_hits = Mock(
            return_value=[
                {"info":{
                    "authors":{"author":
                        {"@pid":"k/DonaldEKnuth","text":"Donald E. Knuth"}},
                    "title":"Companion to the papers of Donald Knuth.",
                    "venue":"CSLI lecture notes series",
                    "volume":"202",
                    "pages":"I-XIII, 1-441",
                    "publisher":"Cambridge University Press",
                    "year":"2012",
                    "type":"Books and Theses",
                    "access":"closed",
                    "key":"books/daglib/0030428",
                    "ee":"http://cslipublications.stanford.edu/site/9781575866345.shtml",
                    "url":"https://dblp.org/rec/books/daglib/0030428"}},
                {"info":{
                    "authors":{"author":
                        {"@pid":"g/WilliamIGasarch","text":"William I. Gasarch"}},
                    "title":"Review of - Algorithmic Barriers Falling - P=NP? by Donald E. Knuth and Edgar G. Daylight and The Essential Knuth by Donald E. Knuth and Edgar G. Daylight.",
                    "venue":"SIGACT News",
                    "volume":"46",
                    "number":"2",
                    "pages":"21-22",
                    "year":"2015",
                    "type":"Journal Articles",
                    "access":"closed",
                    "key":"journals/sigact/Gasarch15e",
                    "doi":"10.1145/2789149.2789155",
                    "ee":"https://doi.org/10.1145/2789149.2789155",
                    "url":"https://dblp.org/rec/journals/sigact/Gasarch15e"}}])

        publications = get_publications(q='Donald E. Knuth')

        self.assertEqual(publications[0].authors[0], 'Donald E. Knuth')
        self.assertEqual(publications[0].title, 'Companion to the papers of Donald Knuth.')
        self.assertEqual(publications[0].venue, 'CSLI lecture notes series')
        self.assertEqual(publications[0].volume, '202')
        self.assertEqual(publications[0].pages, 'I-XIII, 1-441')
        self.assertEqual(publications[0].year, '2012')
        self.assertEqual(publications[0].type, 'Books and Theses')
        self.assertEqual(publications[0].access, 'closed')
        self.assertEqual(publications[0].key, 'books/daglib/0030428')
        self.assertEqual(publications[0].ee, 'http://cslipublications.stanford.edu/site/9781575866345.shtml')
        self.assertEqual(publications[0].url, 'https://dblp.org/rec/books/daglib/0030428')

        self.assertEqual(publications[1].authors[0], 'William I. Gasarch')
        self.assertEqual(publications[1].title, 'Review of - Algorithmic Barriers Falling - P=NP? by Donald E. Knuth and Edgar G. Daylight and The Essential Knuth by Donald E. Knuth and Edgar G. Daylight.')
        self.assertEqual(publications[1].venue, 'SIGACT News')
        self.assertEqual(publications[1].volume, '46')
        self.assertEqual(publications[1].number, '2')
        self.assertEqual(publications[1].pages, '21-22')
        self.assertEqual(publications[1].year, '2015')
        self.assertEqual(publications[1].type, 'Journal Articles')
        self.assertEqual(publications[1].access, 'closed')
        self.assertEqual(publications[1].key, 'journals/sigact/Gasarch15e')
        self.assertEqual(publications[1].doi, '10.1145/2789149.2789155')
        self.assertEqual(publications[1].ee, 'https://doi.org/10.1145/2789149.2789155')
        self.assertEqual(publications[1].url, 'https://dblp.org/rec/journals/sigact/Gasarch15e')