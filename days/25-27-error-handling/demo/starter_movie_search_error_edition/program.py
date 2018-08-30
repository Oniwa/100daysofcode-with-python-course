# import api
#
#
# def main():
#     keyword = 'Python' # input('Keyword of title search: ')
#     results = api.find_movie_by_title(keyword)
#
#     print(f'There are {len(results)} movies found.')
#     for r in results:
#         print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
#
#
# if __name__ == '__main__':
#     main()
import re

def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    pat = re.compile(r'<p>.*?</p>')
    m = pat.search(html)
    return m.group()

print(match_first_paragraph())