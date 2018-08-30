import bs4

def scrape(site):
    soup = bs4.BeautifulSoup(site, 'html.parser')
    html_header_list = soup.select('span.deck-price-paper')

    for item in html_header_list:
        if item.text != '\n':
            print(item.text.strip('\n'))


if __name__ == "__main__":
    with open('.\scraped_page.html') as f:
        site = f.read()

    scrape(site)
