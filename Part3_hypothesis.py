# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:26:50 2016

@author: Aeint Thet Ngon
"""
import pandas as pd
import os
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

'''
Stocks from banking and finance industry
Goldman Sachs Group Inc. GS
American International Group Inc. AIG
JPMorgan Chase & Co. JPM
Aegon AEG
Credit Suisse Group CS
Barclays BCS
Royal Bank of Scotland Group RBS
Deutsche Bank DB
Bank of America Corp. BAC
American Express Co. AXP
'''
tickernames= ['GS', 'AIG', 'JPM', 'AEG', 'CS', 'BCS', 'RBS', 'DB', 'BAC', 'AXP']
entertainment=["DIS", "FOXA", "IMAX", "TWX", "CNK"]
techtick=["AAPL", "MSFT", "INTC", "IBM", "ORCL"]
retailtick=["M", "JCP", "TGT", "WMT", "SHLD"]
financetick=["GS", "AIG", "JPM", "AEG", "CS"]
bankingtick= ["BCS", "RBS", "DB", "BAC", "AXP"]

dir=os.path.dirname(__file__)

'''

etain=list(functionname(entertainment).values())
retail=list(functionname(retailtick).values())
tech=list(functionname(techtick).values())
banking=list(functionname(bankingtick).values())
finance=list(functionname(financetick).values())

'''


#print(myData[myData.Date=="2008-08-01"]['Adj Close'])
#print(myData[:10])
#print(pd.date_range("2007-08-01", "2007-09-01"))

def functionname(params, date):
    droppercent={}
    for i in params:
        filename=i+'_old.csv'
        name=i
        myData=pd.read_csv(os.path.join(dir, 'Data', filename))
        x=len(myData)
        partial=myData[x-30:x]
        least=myData[myData.Date==date]['Adj Close']
        avg=partial["Adj Close"].mean()
        drop1=partial["Adj Close"].mean()- least
        dropper=drop1/avg
        #minOpen={name: least}
        #avgOpen={name: avg}
        #dropval={name: drop1}
        dropp={name: dropper}
        #minVal.update(minOpen)
        #avgVal.update(avgOpen)
        #drop.update(dropval)
        droppercent.update(dropp)
    return(sum(droppercent.values()))

#daterange=pd.bdate_range("2008-09-18", "2008-10-19")    
#daterange=pd.bdate_range("2008-09-28", "2008-10-31")
#daterange=pd.bdate_range("2008-09-02", "2008-10-31")
daterange=pd.bdate_range("2009-03-01", "2009-03-12")
#
#dows={}
#for i in daterange:
#    val={i: functionname(['DJIA'], str(i.date())).iloc[0]}
#    dows.update(val)
##print(dows)
#
#finance={}
#for i in daterange:
#    val={i: functionname(financetick, str(i.date())).iloc[0]}
#    finance.update(val)
##print(finance)
#
#banking={}
#for i in daterange:
#    val={i: functionname(bankingtick, str(i.date())).iloc[0]}
#    banking.update(val)
##print(banking)
#
#etain={}
#for i in daterange:
#    val={i: functionname(entertainment, str(i.date())).iloc[0]}
#    etain.update(val)
##print(etain)
#
#tech={}
#for i in daterange:
#    val={i: functionname(techtick, str(i.date())).iloc[0]}
#    tech.update(val)
##print(tech)
#
#retail={}
#for i in daterange:
#    val={i: functionname(retailtick, str(i.date())).iloc[0]}
#    retail.update(val)
##print(retail)
    
#print({k: dows[k] / float(finance[k]) for k in retail if k in dows}.values())

#dows={}
#for i in daterange:
#    val={i: functionname(['DJIA'], str(i.date())).iloc[0]*0.14602128057775}
#    dows.update(val)
##print(dows)
#
#finance={}
#for i in daterange:
#    val={i: (4/5)*functionname(financetick, str(i.date())).iloc[0]}
#    finance.update(val)
##print(finance)
#
#banking={}
#for i in daterange:
#    val={i: (2/5)*functionname(bankingtick, str(i.date())).iloc[0]}
#    banking.update(val)
##print(banking)
#
#etain={}
#for i in daterange:
#    val={i: (1/5)*functionname(entertainment, str(i.date())).iloc[0]}
#    etain.update(val)
##print(etain)
#
#tech={}
#for i in daterange:
#    val={i:functionname(techtick, str(i.date())).iloc[0]}
#    tech.update(val)
##print(tech)
#
#retail={}
#for i in daterange:
#    val={i: (2/5)*functionname(retailtick, str(i.date())).iloc[0]}
#    retail.update(val)
##print(retail)

#daterange=pd.bdate_range("2008-09-02", "2008-10-31")
daterange=pd.bdate_range("2009-03-01", "2009-03-12")

dows={}
for i in daterange:
    val={i: functionname(['DJIA'], str(i.date())).iloc[0]*0.14602128057775}
    dows.update(val)
sdows=dict(sorted(dows.items()))
#print(dows)

finance={}
for i in daterange:
    val={i: (4/30)*functionname(financetick, str(i.date())).iloc[0]}
    finance.update(val)
sfinance=dict(sorted(finance.items()))
#print(finance)

banking={}
for i in daterange:
    val={i: (2/30)*functionname(bankingtick, str(i.date())).iloc[0]}
    banking.update(val)
sbanking=dict(sorted(banking.items()))
#print(banking)

etain={}
for i in daterange:
    val={i: (1/30)*functionname(entertainment, str(i.date())).iloc[0]}
    etain.update(val)
setain=dict(sorted(etain.items()))
#print(etain)

tech={}
for i in daterange:
    val={i:(5/30)*functionname(techtick, str(i.date())).iloc[0]}
    tech.update(val)
stech=dict(sorted(tech.items()))
#print(tech)

retail={}
for i in daterange:
    val={i: (2/30)*functionname(retailtick, str(i.date())).iloc[0]}
    retail.update(val)
sretail=sorted(retail.items())

X_var=pd.DataFrame()
X_var['Dow']=dows.values()
Y_var=pd.DataFrame() 
Y_var["finance"]=finance.values()
Y_var['banking']=banking.values()
Y_var['tech']=tech.values()
Y_var['etain']=etain.values()
Y_var['retail']=retail.values()

regr = linear_model.LinearRegression()
regr.fit(X_var, Y_var)

print('Coefficients: \n', regr.coef_)

def functionname2(params, date):
    droppercent={}
    for i in params:
        filename=i+'_new.csv'
        name=i
        myData=pd.read_csv(os.path.join(dir, 'Data', filename))
        myData=myData.iloc[::-1]
        partial=myData[170:200]
        least=myData[myData.Date==date]['Adj Close']
        avg=partial["Adj Close"].mean()
        drop1=partial["Adj Close"].mean()- least
        dropper=drop1/avg
        #minOpen={name: least}
        #avgOpen={name: avg}
        #dropval={name: drop1}
        dropp={name: dropper}
        #minVal.update(minOpen)
        #avgVal.update(avgOpen)
        #drop.update(dropval)
        droppercent.update(dropp)
    return(sum(droppercent.values()))
#
#from bokeh.charts import TimeSeries, show, output_file
#myData=pd.read_csv(os.path.join(dir, 'Data', "DJIA_new.csv"))
#myData=myData.iloc[::-1]
#output_file("result.html")
#
#TOOLS='hover'
#data = dict(DJIA=myData['Adj Close'], Date=myData['Date'])
#
##print(data)
#p=TimeSeries(data, x="Date", title="DJIA", tools=TOOLS)
#show(p)

#print(myData[:10])

daterange2=pd.bdate_range("2016-02-04", "2016-02-12")

ndows={}
for i in daterange2:
    val={i: functionname2(['DJIA'], str(i.date())).iloc[0]*0.14602128057775}
    ndows.update(val)
#sdows=dict(sorted(ndows.items()))
#print(ndows)

nfinance={}
for i in daterange2:
    val={i: (4/30)*functionname2(financetick, str(i.date())).iloc[0]}
    nfinance.update(val)
#sfinance=dict(sorted(nfinance.items()))
#print(finance)

nbanking={}
for i in daterange2:
    val={i: (2/30)*functionname2(bankingtick, str(i.date())).iloc[0]}
    nbanking.update(val)
#sbanking=dict(sorted(banking.items()))
#print(banking)

netain={}
for i in daterange2:
    val={i: (1/30)*functionname2(entertainment, str(i.date())).iloc[0]}
    netain.update(val)
#setain=dict(sorted(etain.items()))
#print(etain)

ntech={}
for i in daterange2:
    val={i:(5/30)*functionname2(techtick, str(i.date())).iloc[0]}
    ntech.update(val)
#stech=dict(sorted(tech.items()))
#print(tech)

nretail={}
for i in daterange2:
    val={i: (2/30)*functionname2(retailtick, str(i.date())).iloc[0]}
    nretail.update(val)

NX_var=pd.DataFrame()
NX_var['Dow']=ndows.values()
NY_var=pd.DataFrame() 
NY_var["finance"]=nfinance.values()
NY_var['banking']=nbanking.values()
NY_var['tech']=ntech.values()
NY_var['etain']=netain.values()
NY_var['retail']=nretail.values()

regr = linear_model.LinearRegression()
regr.fit(NX_var, NY_var)

print('Coefficients: \n', regr.coef_)

#main=Y_var
#main['Dow']=dows.values()
#main['Date']= 
#from bokeh.charts import TimeSeries, show, output_file
#from bokeh.layouts import column
#import numpy as np
#nytimes=pd.read_csv("C:/Users/Aeint Thet Ngon/Documents/Project3/NYTarticles_score.csv")
##nytimes[nytimes.title!='NaN']
##print(nytimes[:10])
#
#mydata=pd.DataFrame()
#mydata['Date']=nytimes['date'][nytimes.date!="NaN"]
#mydata['score']=nytimes['sentiment score'][nytimes.title!='NaN']
#print(mydata)
#output_file("sentiment.html")
#p=TimeSeries(mydata, x='Date', y='score')
#show(p)

#from bokeh.charts import TimeSeries, show, output_file
#from bokeh.layouts import column
#
#myData=pd.DataFrame()
#myData['Dow']=ndows.values()
#myData["finance"]=nfinance.values()
#myData['banking']=nbanking.values()
#myData['tech']=ntech.values()
#myData['etain']=netain.values()
#myData['retail']=nretail.values()
#myData['Date']=pd.bdate_range("2016-02-04", "2016-02-12")
#
#output_file("change16.html")
#TOOLS="hover"
#y08=TimeSeries(myData, x="Date", y=['Dow','Finance', "Banking", "Technology", "Entertainment", "Retail"], 
#               color= ['Dow','Finance', "Banking", "Technology", "Entertainment", "Retail"], 
#                dash= ['Dow','Finance', "Banking", "Technology", "Entertainment", "Retail"], 
#                tools=TOOLS, title="Changes of different industry in 2016")
#
##y16=TimeSeries(djia16, x="Date", y="Adj Close",tools=TOOLS, title="DJIA from mid 2014 to now", plot_height=280)
#
#show(y08)
#
#print(myData)