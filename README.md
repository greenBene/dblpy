# dblpy
**Dblpy** is a simple wrapper library for the dblp.org search api.

```py
from dblpy import get_authors, get_venues, get_publications

authors = get_authors(q='Donald Knuth')
for a in authors:
    print(a)

    for n in a.notes:
        print(f'|{n}')

publications = get_publications(q='gps trajectory', max_results=5)
for p in publications:
    print(p)

venues = get_venues(q='Berlin')
for v in venues:
    print(v)
```

## Installing Dblpy
`$pip3 install dblpy-lib`

## Using the Library
The library offers functions to query dblp.org for publications, authors, and venues. They return lists of the respective objects.

For some publications, authors, or venues, not all possible attributes are available. In these cases, they are set to an empty string.

You can limit the number of results with the argument `max_results=X`. This is set by default to 100.

### Authors 
```py
authors = get_authors(q='Donald Knuth', max_results=10)
author = authors[0]

author.name # Name of Author
author.notes # List of affiliations and awards linked to author
author.notes[0].type # Type of affiliation
author.notes[0].text # Name of affiliation
author.aliases # List of other names of same author
author.url # Link to dblp page of author
```

### Publications

```py
publications = get_publications(q='gps trajectory', max_results=5)
publ = publications[0]

publ.authors # List of author names 
publ.title # Name of publication
publ.venue # Venue of publication
publ.volume # Volume in which publication was published
publ.number # Number of publication volume
publ.pages # Pages of publication 
publ.publisher # Publisher of publication
publ.year # Year when publication was released
publ.type # Type of publication
publ.access # Type of access
publ.key # Key of publication
publ.doi # Doi of publication 
publ.ee # Link to electronic edition of publication
publ.url # Link to dblp page of publication
```

### Venues
```py
venues = get_venues(q='Berlin', max_results=5)
venue = venues[0]

venue.name # Name of venue
venue.acronym # Acronym of venue
venue.type # Type of venue
venue.url # Link to dblp page of venue
```
