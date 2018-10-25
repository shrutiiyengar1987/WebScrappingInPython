import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://+Urlname",headers=headers)

content = response.content
soup = BeautifulSoup(content,"html.parser")

collection_info=soup.find_all("div" ,attrs={"class": "class name of the div which is the parent collection "})
list_tr=collection_info[0].find_all(True,attrs={"class":"class name of the child collections "})


list_elements=[]
for tr in list_tr:
    dataframe ={}
    dataframe["element_attribute1"] = (tr.find(True,attrs={"class": "attribute 1 classname"})).text.replace('\n', ' ')
    dataframe["element_attribute2"] = (tr.find(True,attrs={"class": "attribute 2 class name"})).text.replace('\n', ' ')
    list_elements.append(dataframe)
list_elements 

import pandas
df = pandas.DataFrame(list_elements)
df.to_csv("data.csv",index=False)
