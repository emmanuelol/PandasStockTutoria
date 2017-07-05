# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:08:28 2017

@author: ledra
"""
import os
import plotly as py
import plotly.graph_objs as go

from datetime import datetime
import pandas_datareader.data as web

df = web.DataReader("aapl", 'google',
                    datetime(2007, 1, 1))

print (df.head())
print("Max Close",df['Close'].max())
print("Volume mean",df['Volume'].mean())
data = [go.Scatter(x=df.index, y=df.High)]

py.offline.plot(data)
