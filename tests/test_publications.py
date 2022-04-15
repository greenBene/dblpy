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
            pages='I-XIII, 1-441',
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
            pages='I-XIII, 1-441',
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
                {'info': {
                    'authors': {'author': [
                        {'@pid': '257/4981', 'text': 'Nicolas J. Lehmann'}, 
                        {'@pid': '287/7466', 'text': 'Muhammed-Ugur Karagülle'}, 
                        {'@pid': '287/7489', 'text': 'Felix Spielmann'}, 
                        {'@pid': '287/7467', 'text': 'Bianca George'}, 
                        {'@pid': '304/1821', 'text': 'Benjamin Zick'}, 
                        {'@pid': '304/1756', 'text': 'Joel Heuer'}, 
                        {'@pid': '304/1753', 'text': 'Eike Taegener'}, 
                        {'@pid': '304/1894', 'text': 'Abd Alah Fahed'}, 
                        {'@pid': 'v/AVoisard', 'text': 'Agnès Voisard'}, 
                        {'@pid': '287/7475', 'text': 'Joachim W. Fluhr'}]}, 
                    'title': 'mHealthAtlas - An expert-based multi-sided platform for the evaluation of mHealth applications.', 
                    'venue': 'ICHI', 
                    'pages': '449-450', 
                    'year': '2021', 
                    'type': 'Conference and Workshop Papers', 
                    'access': 'closed', 
                    'key': 'conf/ichi/LehmannKSGZHTFV21', 
                    'doi': '10.1109/ICHI52183.2021.00079', 
                    'ee': 'https://doi.org/10.1109/ICHI52183.2021.00079', 
                    'url': 'https://dblp.org/rec/conf/ichi/LehmannKSGZHTFV21'}}, 
                {'info': {
                    'authors': {'author': [
                        {'@pid': '257/4981', 'text': 'Nicolas J. Lehmann'}, 
                        {'@pid': '287/7489', 'text': 'Felix Spielmann'}, 
                        {'@pid': '287/7467', 'text': 'Bianca George'}, 
                        {'@pid': '290/5424', 'text': 'Linus Ververs'}, 
                        {'@pid': '287/7466', 'text': 'Muhammed-Ugur Karagülle'}, 
                        {'@pid': '287/7480', 'text': 'Daniel Kmiotek'}, 
                        {'@pid': '290/5366', 'text': 'Laura Mielke'}, 
                        {'@pid': '287/7504', 'text': 'Oliver Junk'}, 
                        {'@pid': 'v/AVoisard', 'text': 'Agnès Voisard'}, 
                        {'@pid': '287/7475', 'text': 'Joachim W. Fluhr'}]}, 
                    'title': 'mHealthAtlas - An Approach for the Multidisciplinary Evaluation of mHealth Applications.', 
                    'venue': 'HealthCom', 
                    'pages': '1-5', 
                    'year': '2020', 
                    'type': 'Conference and Workshop Papers', 
                    'access': 'closed', 
                    'key': 'conf/healthcom/LehmannSGVKKMJV20', 
                    'doi': '10.1109/HEALTHCOM49281.2021.9399045', 
                    'ee': 'https://doi.org/10.1109/HEALTHCOM49281.2021.9399045', 
                    'url': 'https://dblp.org/rec/conf/healthcom/LehmannSGVKKMJV20'}}])

        publications = get_publications(q='mHealthAtlas')
        self.assertEqual(publications[0].title, 'mHealthAtlas - An expert-based multi-sided platform for the evaluation of mHealth applications.')
        self.assertEqual(publications[1].title, 'mHealthAtlas - An Approach for the Multidisciplinary Evaluation of mHealth Applications.')