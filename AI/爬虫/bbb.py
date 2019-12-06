import requests as r
ad=r.get('http://www.tianqihoubao.com/lishi/guilin/month/201910.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(ad.text, 'html.parser', from_encoding='utf-8')
lili=soup.find_all('div',class_="months")
print('w')
#%%
soups = BeautifulSoup(lili.__str__(), 'html.parser', from_encoding='utf-8')
lili=soups.find_all('a')
lis =list()
for y in lili:
    lis.append(y.get('href'))
print(lis)

#%%
import pandas as pd
for tt in lis:
    url ='http://www.tianqihoubao.com'+tt
    a=r.get(url)
    tb = pd.read_html(a.text)[0]
    print(tb)