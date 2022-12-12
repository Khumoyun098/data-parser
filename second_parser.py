"""
    Parser for kun.uz
"""
from typing import List
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

base_url = "https://kun.uz"
mobile_base_url = "https://m.kun.uz"
news_list_url = "https://kun.uz/uz/news/list"

s = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 "
                  "Safari/537.36 "
}

r = s.get(url=news_list_url, headers=headers)

soup = bs(r.content, "html.parser")
posts = soup.find_all("a", {"class": "daily-block l-item"})

container = []

for post in posts:
    container.append(post['href'])


def limiter(start: int = 1, limit: int = 10000):
    next_page = soup.find_all("a", {"class": "load-more__link next"})[0]
    while start < limit:
        e = s.get(url=base_url + next_page["href"], headers=headers)
        osh = bs(e.content, "html.parser")
        i_posts = osh.find_all("a", {"class": "daily-block l-item"})
        for f_post in i_posts:
            container.append(f_post['href'])
        next_page = osh.find_all("a", {"class": "load-more__link next"})[0]
        start += 1
    return container


def body_collector(endpoint: str) -> str:
    result = []
    url = mobile_base_url + endpoint
    inner_request = requests.get(url=url, headers=headers)
    inner_soup = bs(inner_request.content, "html.parser")
    body_content = inner_soup.find_all("div", {"class": "post post-details"})
    for content in body_content:
        for treator in content.findAll('p'):
            if len(treator.text.strip()) > 0:
                result.append(treator.text.strip())
    return " ".join(result)


limiter()


def major_parser(container: List) -> List:
    res = []
    for p in container:
        res.append({
            "source_url": mobile_base_url + p,
            "access_datetime": int(time.time()),
            "content": body_collector(p)
        })
    return res


df = pd.DataFrame.from_dict(major_parser(container))
df.to_csv(r'kun_uz.csv', index=False, header=True)
