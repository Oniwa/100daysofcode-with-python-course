from collections import defaultdict, namedtuple, Counter
import csv

beer = namedtuple('beer', 'name style brewery_id')
brew_name = namedtuple('brew_name', 'id name state')

brewery_names = defaultdict(list)
with open('breweries.csv') as f:
    for line in csv.DictReader(f):
        try:
            id = line['']
            name = line['name']
            state = line['state']
        except ValueError:
            continue

        brew = brew_name(id=id, name=name, state=state)
        brewery_names[id].append(brew)

brewerys = defaultdict(list)
with open('beers.csv') as f:
    for line in csv.DictReader(f):
        try:
            brewery = line['brewery_id']
            style = line['style']
            name = line['name']
        except ValueError:
            continue

        b = beer(name=name, style=style, brewery_id=brewery)

        brewerys[brewery].append(b)

cnt = Counter()
for brewery_id, name in brewerys.items():
    cnt[brewery_names[brewery_id][0].name] += len(name)

print(cnt.most_common(5))

cnt2 = Counter()
for brewery_id, beers in brewerys.items():
    cnt2[beers[0].style] += 1

print(cnt2.most_common(5))