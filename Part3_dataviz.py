import numpy as np
import pandas as pd
from bokeh.plotting import *
from bokeh.models import ColumnDataSource
import os
from bokeh.charts import TimeSeries, show, output_file
from bokeh.layouts import column

dir=os.path.dirname(__file__)
djia8=pd.read_csv(os.path.join(dir, 'Data', "DJIA_old.csv"), parse_dates=['Date'])
djia8=djia8.iloc[::-1]
djia16=pd.read_csv(os.path.join(dir, 'Data', "DJIA_new.csv"), parse_dates=['Date'])
djia16=djia16.iloc[::-1]

#date=djia8['Date']
#date8=[]
#for i in range(0,len(date)):
#    match = re.search('\d{4}', date[i])
#    date8.append(match.group(0))
#output_file("Djia.html")
#TOOLS="lasso_select, hover"
#djia8['Date']=date8
#
#date=djia16['Date']
#date16=[]
#for i in range(0,len(date)):
#    match = re.search('\d{4}', date[i])
#    date16.append(match.group(0))
#
#djia16['Date']=date16
#
#print(djia16[:10])




output_file("Djia.html")
TOOLS="hover"
y08=TimeSeries(djia8, x="Date", y="Adj Close", tools=TOOLS,title="DJIA from mid 2007 to mid 2009", plot_height=280)

y16=TimeSeries(djia16, x="Date", y="Adj Close",tools=TOOLS, title="DJIA from mid 2014 to now", plot_height=280)

show(y16)



#tickernames= ['GS', 'AIG', 'JPM', 'AEG', 'CS', 'BCS', 'RBS', 'DB', 'BAC', 'AXP']
#
#aig8=pd.read_csv(os.path.join(dir, 'Data', "aig_old.csv"))
#aig8=aig8.iloc[::-1]
#jpm8=pd.read_csv(os.path.join(dir, 'Data', "jpm_old.csv"))
#jpm8=jpm8.iloc[::-1]
#rbs8=pd.read_csv(os.path.join(dir, 'Data', "rbs_old.csv"))
#rbs8=rbs8.iloc[::-1]
#db8=pd.read_csv(os.path.join(dir, 'Data', "db_old.csv"))
#db8=db8.iloc[::-1]
#
#output_file("Stock.html")
#data = dict(
#    AIG=aig8['Adj Close'],
#    Date=aig8['Date'],
#    JPM=jpm8['Adj Close'],
#    RBS=rbs8['Adj Close'],
#    DB=db8['Adj Close']
#)
#
#tsline = TimeSeries(data,
#    x='Date', y=['AIG', 'JPM', "RBS", "DB"],
#    color=['AIG', 'JPM', "RBS", "DB"], dash=['AIG', 'JPM', "RBS", "DB"],
#    title="Timeseries", ylabel='Stock Prices', legend=True)
#tsline.xaxis.visible=False
#
#show(tsline)
##
#
#foxsent=pd.read_csv(os.path.join(dir, 'Data', "foxnews_score.csv"), sep=',', encoding='latin1')
#nytsent=pd.read_csv(os.path.join(dir, 'Data', "NYTarticles_score.csv"), sep=',', encoding='latin1')
#
#foxsent['date']=pd.to_datetime(foxsent['date'])
#nytsent['date']=pd.to_datetime(nytsent['date'])
#
#df=pd.DataFrame()
#df['Date']=foxsent['date']
#df['sentiment']=foxsent['sentiment score']
#df.groupby('Date').sum()
#
#df.to_csv("foxsentbydate.csv", sep=',', encoding='utf-8')
#
#df2=pd.DataFrame()
#df2['Date']=nytsent['date']
#df2['sentiment']=nytsent['SentimentScore']
#df2.groupby('Date').sum()
#
#df2.to_csv("nytsentbydate.csv", sep=',', encoding='utf-8')
#df.set_index('Date').join(df2.set_index('Date'))
#print(df)

