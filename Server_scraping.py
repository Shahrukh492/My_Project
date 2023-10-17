import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.hubertiming.com/results/2018MLK'
html=urlopen(url)
soup=BeautifulSoup(html)
title=soup.title
#Print the title
print(title.text)
links=soup.find_all('a')
#Print the Links
print(links)
for link in links:
    print(link.get('href'))

#Print the Data Frame
data=[]
allrows=soup.find_all('tr')
for row in allrows:
    row_list=row.find_all('td')
    dataRow=[]
for cell in row_list:
    dataRow.append(cell.text)
    data.append(dataRow)
    data=data[1:]
    print(data[1:])
