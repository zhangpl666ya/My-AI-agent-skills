import requests
from bs4 import BeautifulSoup

def get_webpage_text(url:str)->str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"}
    r = requests.get(url,headers = headers,timeout = 10)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,"html.parser")

    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text() for p in paragraphs)
    return text[:5000]

def local_llm(prompt:str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json = {
            "model":"llama3.2",
            "prompt":prompt,
            "stream":False
        }
    )
    return response.json()["response"]

def summarize_webpage(url:str):
    text = get_webpage_text(url)
    prompt = f"""
    请帮我总结下面网页内容，提取重点：
    {text}
"""
    summary = local_llm(prompt)
    return summary