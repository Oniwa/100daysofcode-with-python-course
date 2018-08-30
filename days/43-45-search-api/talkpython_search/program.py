import webbrowser

import api


def main():
    keyword = input('What are you looking for? ')
    results = api.search_talk_python(keyword)

    print(f'There are {len(results)} matching episodes:')
    for idx, episode in enumerate(results):
        print(f'{int(idx) + 1}. {episode.category} - {episode.title}')

    choice = input('If you would like to view a result enter the number or '
                   'enter anything else to exit: ')
    if choice.isdigit():
        webbrowser.open(f'https://talkpython.fm{results[int(choice) - 1].url}',
                        new=2)


if __name__ == '__main__':
    main()
