import unittest

from dblpy import Venue, get_venues
from dblpy.dblp_api import DblpAPI
from unittest.mock import Mock

class VenuesTestCase(unittest.TestCase):
    def test_creating_venue(self):
        venue = Venue(
            venue='Electronic Information, the Visual Arts and Beyond Conference (EVA)',
            acronym='EVA',
            type='Conference or Workshop',
            url='https://dblp.org/db/conf/evaconf/'
        )

        self.assertEqual(venue.venue, 'Electronic Information, the Visual Arts and Beyond Conference (EVA)')
        self.assertEqual(venue.acronym, 'EVA')
        self.assertEqual(venue.type, 'Conference or Workshop')
        self.assertEqual(venue.url, 'https://dblp.org/db/conf/evaconf/')

    def test_print_venue(self):
        venue = Venue(
            venue='Electronic Information, the Visual Arts and Beyond Conference (EVA)',
            acronym='EVA',
            type='Conference or Workshop',
            url='https://dblp.org/db/conf/evaconf/'
        )

        self.assertEqual(str(venue), 'Electronic Information, the Visual Arts and Beyond Conference (EVA) (https://dblp.org/db/conf/evaconf/)')

    def test_get_venues(self):
        DblpAPI.load_hits = Mock(
            return_value=[{
                "info":{
                    "venue":"Berlin Workshops",
                    "type":"Conference or Workshop",
                    "url":"https://dblp.org/db/conf/berlin/"},
                },
                {"info":{
                    "venue":"Electronic Information, the Visual Arts and Beyond Conference (EVA)",
                    "acronym":"EVA",
                    "type":"Conference or Workshop",
                    "url":"https://dblp.org/db/conf/evaconf/"}}])
        venues = get_venues(q='Berlin')
        self.assertEqual(venues[0].venue, 'Berlin Workshops')
        self.assertEqual(venues[0].type, 'Conference or Workshop')
        self.assertEqual(venues[0].url, 'https://dblp.org/db/conf/berlin/')
        self.assertEqual(venues[1].venue, 'Electronic Information, the Visual Arts and Beyond Conference (EVA)')
        self.assertEqual(venues[1].acronym, 'EVA')
        self.assertEqual(venues[1].type, 'Conference or Workshop')
        self.assertEqual(venues[1].url, 'https://dblp.org/db/conf/evaconf/')
