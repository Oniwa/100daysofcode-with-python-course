import feedparser

FEED_FILE = "channelfireball.xml"

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        if 'Pauper' in entry.title:
            print(f'{entry.published} - {entry.title}: {entry.link}')
