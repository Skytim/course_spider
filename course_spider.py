# -*- coding: utf-8 -*-
__author__ = 'SkyTim'

from bs4 import BeautifulSoup
import urllib2
import unicodecsv

for x in range(3):
    for y in range(10):
        url="http://newdoc.nccu.edu.tw/teaschm/1032/statistic.jsp-tnum=3060"+str(x)+str(y)+".htm"
        try:
            page=urllib2.urlopen(url)
            soup = BeautifulSoup(page)
            fileName=soup.br.previous_element.get_text()
            f=open("csv/"+fileName[5:]+".txt", "w")
            w=unicodecsv.writer(f)
            row=[]
            for article in soup.find_all('a'):
                row.append([article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element,article.previous_element.previous_element])
            w.writerows(row)
            f.close()
        except urllib2.HTTPError, err:
            print(err.code)





