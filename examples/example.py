from dblpy import get_authors, get_venues, get_publications

print('--------SEARCH FOR AUTHORS--------')
authors = get_authors(q='Donald Knuth')

for a in authors:
    print(a.name)

    for n in a.notes:
        print(f'|{n}')

print('--------SEARCH FOR PUBLICATIONS--------')
publications = get_publications(q='gps trajectory', max_results=5)

for p in publications:
    print(p)

print('--------SEARCH FOR VENUES--------')
venues = get_venues(q='Berlin')

for v in venues:
    print(v)