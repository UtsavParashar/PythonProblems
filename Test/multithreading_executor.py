from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistent-subdomain.python.org/']

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
    
with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_url = {executor.submit(load_url, url, 60):url for url in URLS}

    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as ex:
            print(f'{url} generated an exception {ex}')
        else:
            print(f'{url} page is {len(data)} bytes.')