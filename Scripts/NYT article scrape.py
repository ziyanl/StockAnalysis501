# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:25:55 2016

@author: Aeint Thet Ngon
"""
#reference: 
    #1. http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial
    #2. http://stackoverflow.com/questions/18841248/ny-times-api-and-scrapy

import requests
import csv
from time import sleep

csvName="NYTarticles.csv"

#the function will get the articles within the start date and end date with articles including the query
# i is the page number, it is not iterated in the loop because of the api call limit
# it'll write the publication date, headline, and abstract to a csv file
def getarticles(startdate, enddate, query, i):
    start='http://api.nytimes.com/svc/search/v2/articlesearch.json?q='
    url=start + query + '& page=' + str(i) + '&sort=newest' + '&begin_date=' + startdate + '&end_date=' + enddate + '&api-key=d0fc2916c9d049e1b3ff253cdb89685a'
    response=requests.get(url)
    jv=response.json()
    for doc in jv['response']['docs']:
        s=[doc['pub_date'].split("T")[0],doc['headline']['main'],doc['abstract']]
        with open(csvName, "a") as articleFile:
            articlewriter = csv.writer(articleFile)
            articlewriter.writerow(s)

#for loop for page numbers to be written to csv file, had to sleep for 6 seconds, since only 1 call allowed by 5seconds
for i in range(1, 50):
    print(i)
    getarticles('20160101','20160901', 'stock+market', i)
    sleep(6)

for i in range(1,20):
    print(i)
    getarticles("20150101", "20151231", "stock+market", i)
    sleep(6)
