import requests
from bs4 import BeautifulSoup

def get_webpage_info(url: str):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string if soup.title else "无标题"
    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text() for p in paragraphs)
    return {
        "title": title,
        "content": text  # 注意这里是 content，和 test.py 里的 key 一致
    }