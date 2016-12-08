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

#function to get the difference percentage and sum it for each day
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
        dropp={name: dropper}
        droppercent.update(dropp)
    return(sum(droppercent.values()))

daterange=pd.bdate_range("2008-09-18", "2008-10-19") #Date range around the financial crisis  
#getting a dictionary for each industry
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

#the sum differnece percentage is weighted according to how many stocks of that industry is in Dow Jones Calculation
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

daterange=pd.bdate_range("2009-03-01", "2009-03-12") #date range for the financial crisis

#getting a dictionary for each industry
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

#function to get the difference percentage and sum it for each day
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
        dropp={name: dropper}
        droppercent.update(dropp)
    return(sum(droppercent.values()))

daterange2=pd.bdate_range("2016-02-04", "2016-02-12")

ndows={}
for i in daterange2:
    val={i: functionname2(['DJIA'], str(i.date())).iloc[0]*0.14602128057775}
    ndows.update(val)
#print(ndows)

nfinance={}
for i in daterange2:
    val={i: (4/30)*functionname2(financetick, str(i.date())).iloc[0]}
    nfinance.update(val)
#print(finance)

nbanking={}
for i in daterange2:
    val={i: (2/30)*functionname2(bankingtick, str(i.date())).iloc[0]}
    nbanking.update(val)
#print(banking)

netain={}
for i in daterange2:
    val={i: (1/30)*functionname2(entertainment, str(i.date())).iloc[0]}
    netain.update(val)
#print(etain)

ntech={}
for i in daterange2:
    val={i:(5/30)*functionname2(techtick, str(i.date())).iloc[0]}
    ntech.update(val)
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
