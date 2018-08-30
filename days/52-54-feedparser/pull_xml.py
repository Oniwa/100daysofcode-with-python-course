import requests
import urllib3

URL = 'http://www.channelfireball.com/feed/'

opener = urllib3.PoolManager()


if __name__ == "__main__":
    r = opener.request('GET', URL)
    with open('channelfireball.xml', 'wb') as f:
        f.write(r.data)
