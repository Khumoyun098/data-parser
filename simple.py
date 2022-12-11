import re
import time
from typing import Dict

import pandas as pd

import requests
from bs4 import BeautifulSoup as bs

target_url = "https://api.uza.uz/api/v1/posts/{post_id}"  # uza.uz

limit_posts = 5
found_list = []
id_counter = 431916

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 "
                  "Safari/537.36 "
}

while len(found_list) < limit_posts:

    sess = requests.Session()
    with sess.get(url=target_url.format(post_id=id_counter), verify=False, headers=headers) as r:
        if r.status_code != 200 or r.status_code == 404:
            continue
        data = r.json()
        # check lang
        if data["lang"] == 2:
            found_list.append(id_counter)
            print("LEN", len(found_list))

        id_counter -= 1
        print("COIN", id_counter)


def text_cleaner(text: str) -> str:
    return re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)


def parser(post_id: int) -> Dict:
    """
    :param post_id:
    :return: {
        "source_url": "post_url",
        "access_datetime": "datetime.now",
        "content": "content"
    }
    """
    source_url = target_url.format(post_id=post_id)
    with sess.get(url=source_url, verify=False, headers=headers) as t:
        t.raise_for_status()
        content = t.json()["content"]
        soup = bs(content, "html.parser")
        text = soup.text
        return {
            "source_url": source_url,
            "access_datetime": int(time.time()),
            "content": ''.join(filter(lambda x: not x.isdigit(), text_cleaner(text.lower())))
        }


container = []
for i in found_list:
    container.append(parser(post_id=i))

df = pd.DataFrame.from_dict(container)
df.to_csv(r'main.csv', index=False, header=True)

