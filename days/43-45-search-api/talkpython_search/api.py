import collections
from typing import List

import requests


Episode = collections.namedtuple('Episode', 'category, id, url, title, '
                                            'description')


def search_talk_python(keyword: str) ->List[Episode]:
    url = f'http://search.talkpython.fm/api/search?q={keyword}'
    matches = []

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    for item in results['results']:
        matches.append(Episode(**item))

    return matches


if __name__ == "__main__":
    print(search_talk_python('test'))
