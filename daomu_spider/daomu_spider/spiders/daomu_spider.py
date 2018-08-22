# -*- coding: utf-8 -*-
import json
import urllib
import urllib.request
import bs4
import os

start_urls = ['http://daomubiji.com/zang-hai-hua/']
os.makedirs('booklist', exist_ok=True)
for url in start_urls:
    html = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html)
    response = soup.select('article > a')
    for item in response:
        text = []
        bookname, chapter, content = item.getText().split(' ')
        download_addr = item.get('href')
        text.append(chapter + ' ' + content)
        text.append(download_addr)
        filename = os.path.join('booklist', chapter  + content + ' ')
        print(download_addr,'Downloading start ....')
        article = urllib.request.urlopen(download_addr).read()
        with open(filename,'wb') as f:
            f.write(article)
        print(download_addr, 'Downloading end ....')
    f.close()
print("ending....")
w = json.dumps(text)
print(w)
file = os.path.join('booklist',bookname + '.txt')
with open(file,'wb') as f:
    f.write(w)
f.close()
