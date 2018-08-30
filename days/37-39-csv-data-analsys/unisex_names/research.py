import os
import csv
import collections
from typing import List

data = []

Record = collections.namedtuple('Record', 'uid,name,total,'
                                          'male_share,female_share,gap')


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'unisex_names_table.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    row[''] = int(row[''])
    row['total'] = float(row['total'])
    row['male_share'] = float(row['male_share'])
    row['female_share'] = float(row['female_share'])
    row['gap'] = float(row['gap'])

    record = Record(row[''], row['name'], row['total'], row['male_share'],
                    row['female_share'], row['gap'])

    return record


def most_male_name() -> List[Record]:
    return sorted(data, key=lambda r: -r.male_share)


def most_female_name() -> List[Record]:
    return sorted(data, key=lambda r: -r.female_share)


def most_unisex_name() -> List[Record]:
    return sorted(data, key=lambda r: r.gap)


if __name__ == '__main__':
    print('Unisex Names')
    init()
    print('The 5 most male unisex names')
    names = most_male_name()
    for idx, d in enumerate(names[:5]):
        print(f'{idx+1} {d.name} with {d.male_share} % Male')
    print('The 5 most female unisex names')
    names = most_female_name()
    for idx, d in enumerate(names[:5]):
        print(f'{idx+1} {d.name} with {d.female_share} % Female')
    print('The 5 most unisex names')
    names = most_unisex_name()
    for idx, d in enumerate(names[:5]):
        print(f'{idx+1} {d.name} with {d.gap} % difference between male '
              f'and female usage')