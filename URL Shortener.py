from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib
import sys

def make_tiny(url):
    request_url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': url})
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def main():
    for tinyurl in map(make_tiny, sys.argv[1:]):
        print(tinyurl)

if __name__ == '__main__':
    main()

def make_tiny(url):
    request_url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': url})
    try:
        with contextlib.closing(urlopen(request_url)) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error creating TinyURL for {url}: {e}")
        return None
