import requests

URL = 'https://www.mtggoldfish.com/metagame/pauper#paper'


def pull_site():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()

    with open('.\scraped_page.html', 'wb') as f:
        f.write(raw_site_page.content)


if __name__ == "__main__":
    pull_site()