from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(URL)
soup=bs(page.text,"html.parser")
startable=soup.find("table")
exolist=[]
tablerows=startable.find_all("tr")
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text for i in td]

    exolist.append(row)

name=[]
dist=[]
mass=[]
radius=[]
lem=[]

for i in range(1,len(exolist)):
    name.append(exolist[i][1])
    dist.append(exolist[i][3])
    mass.append(exolist[i][5])
    radius.append(exolist[i][6])
    lem.append(exolist[i][7])

tf=pd.DataFrame(list(zip(name,dist,mass,radius,lem)),columns=["name","dist","mass","radius","lem"])
tf.to_csv("stars.csv")