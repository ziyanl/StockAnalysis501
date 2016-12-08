import numpy as np
import pandas as pd
from bokeh.plotting import *
from bokeh.models import ColumnDataSource
import os
from bokeh.charts import TimeSeries, show, output_file
from bokeh.layouts import column

dir=os.path.dirname(__file__)

#Reading file from 2016 and 2008
djia8=pd.read_csv(os.path.join(dir, 'Data', "DJIA_old.csv"), parse_dates=['Date'])
djia8=djia8.iloc[::-1] #reorder since they were in reverse 
djia16=pd.read_csv(os.path.join(dir, 'Data', "DJIA_new.csv"), parse_dates=['Date'])
djia16=djia16.iloc[::-1]

#produce the time series of DJIA from the old time period and the new one. 
output_file("Djia.html")
TOOLS="hover"
y08=TimeSeries(djia8, x="Date", y="Adj Close", tools=TOOLS,title="DJIA from mid 2007 to mid 2009", plot_height=280)

y16=TimeSeries(djia16, x="Date", y="Adj Close",tools=TOOLS, title="DJIA from mid 2014 to now", plot_height=280)

show(y16)

