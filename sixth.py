import sys
import requests
import re

def download_url_and_get_all_hrefs(url):

    hrefs = []
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Chyba při stahování URL, status code: {response.status_code}")

    html = response.text

    matches = re.findall(r'<a\s+[^>]*href=["\'](.*?)["\']', html, re.IGNORECASE)

    hrefs = matches
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)

        for link in links:
            print(link)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")