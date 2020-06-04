import requests

import re
import json


def getPage(url):
    response = requests.get(url)
    return response.text


def parsePage(s):
    com = re.compile(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)
    ret = com.finditer(s)
    for i in ret:
        yield {
            "id": i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num"),
        }


def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = getPage(url)
    ret = parsePage(response_html)
    f = open("move_info7", "a", encoding="utf8")
    for obj in ret:
        print(obj)
        data = json.dumps(obj, ensure_ascii=False)
        f.write(data + "\n")


if __name__ == '__main__':
    count = 0
    for i in range(10):
        main(count)
        count += 25