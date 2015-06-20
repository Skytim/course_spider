# -*- coding: utf-8 -*-
__author__ = 'SkyTim'

from bs4 import BeautifulSoup
import urllib2
import unicodecsv

data = open("data.csv", "w")
w = unicodecsv.writer(data)
firstrow = (u'老師', u'課程名稱',u'學年',u'學期', u'分數' )
w.writerow(firstrow)

for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        url="http://newdoc.nccu.edu.tw/teaschm/1032/statistic.jsp-tnum=3"+str(b)+str(c)+str(d)+str(e)+str(f)+".htm"
                        try:
                            page = urllib2.urlopen(url)
                            soup = BeautifulSoup(page)
                            teacherName = soup.br.previous_element.get_text()
                            w = unicodecsv.writer(data)

                            for article in soup.find_all('a'):
                                row = []
                                row.append(([teacherName[10:], article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element,article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element, article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element, article.previous_element.previous_element]))
                                w.writerows(row)
                            for article in soup.find_all(colspan="2"):

                                row = []
                                row.append(([teacherName[10:], article.previous_element.previous_element.previous_element,article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element, article.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element, 70]))
                                w.writerows(row)
                        except urllib2.HTTPError, err:
                            print("無法抓到教師編號3"+str(b)+str(c)+str(d)+str(e)+str(f))




data.close()





