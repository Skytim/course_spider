# -*- coding: utf-8 -*-
__author__ = 'SkyTim'

from bs4 import BeautifulSoup
import urllib2
import unicodecsv

data = open("data.csv", "w")
w = unicodecsv.writer(data)
firstrow = (u'老師', u'課程名稱',u'學年',u'學期', u'分數' )
w.writerow(firstrow)
for x in range(5):
    for y in range(10):
        url="http://newdoc.nccu.edu.tw/teaschm/1032/statistic.jsp-tnum=3060"+str(x)+str(y)+".htm"
        try:
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page)
            teacherName = soup.br.previous_element.get_text()
            w = unicodecsv.writer(data)
            row = []
            for article in soup.find_all('a'):
                row.append(([teacherName[10:], article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element,article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element, article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element, article.previous_element.previous_element]))

                w.writerows(row)

        except urllib2.HTTPError, err:
             print("無法抓到教師編號3060"+str(x)+str(y))
data.close()





