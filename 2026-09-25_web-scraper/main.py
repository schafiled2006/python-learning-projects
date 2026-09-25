import urllib.request
import re
from html import unescape

HEADERS = {"User-Agent": "Mozilla/5.0 (practice-scraper)"}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read().decode("utf-8", errors="replace")

def extract_titles(html):
    """Pull h1/h2 headings out of a page."""
    titles = re.findall(r"<h[12][^>]*>(.*?)</h[12]>", html, re.S)
    return [unescape(re.sub(r"<[^>]+>", "", t)).strip() for t in titles]

if __name__ == "__main__":
    url = input("url: ").strip()
    page = fetch(url)
    for title in extract_titles(page):
        print("-", title)
