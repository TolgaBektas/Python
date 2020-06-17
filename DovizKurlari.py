# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
url ="https://dolar.tlkur.com"
re=requests.get(url)
soup= bs(re.content,'html.parser')
dolar=[soup.find(id="major_rates").text]
print(dolar[0])
input()
