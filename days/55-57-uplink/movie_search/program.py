from api import MovieSearchClient

def main():
    val = input('To search by keyword enter 1, director enter 2, '
                'or IMDB code enter 3.  To exit enter anything else: ')

    svc = MovieSearchClient()

    if val == '1':
        search = input('Enter a keyword: ')

        response = svc.search_keyword(search)

        results = response.json()

        for idx, item in enumerate(results['hits'], 1):
            print(f'{idx}. {item.get("title")}')
    elif val == '2':
        search = input('Enter a director: ')

        response = svc.search_director(search)

        results = response.json()

        for idx, item in enumerate(results['hits'], 1):
            print(f'{idx}. {item.get("title")}')
    elif val == '3':
        search = input('Enter a IMDB code: ')

        response = svc.search_imdb_code(search)

        results = response.json()

        print(results.get('title'))
    else:
        print('Goodbye!')


if __name__ == "__main__":
    main()