# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
url ="https://altin.doviz.com/gram-altin"
re=requests.get(url)
soup= bs(re.content,'html.parser')
altin=[soup.findAll("div", {"class": "data"})]
print(altin[0])
input()
