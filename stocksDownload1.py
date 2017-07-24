# -*- coding: utf-8 -*-
#"""
#Created on Mon Jun 26 13:28:26 2017

# @ author: ledra
##"""

#"""librerias basicas"""

import os #libreria basica de entradas salidas
import pandas as pd #libreria Pandas
from pandas_datareader import data as web # libreria pandas datareader para descargar los stocks directamente
import plotly as py
import plotly.graph_objs as go


def get_data(symbols, dates): #funcion get_data que recibe de entrada las variables symbols y dates
    #"""Read stock data (adjusted close) for given symbols from CSV files."""
    #esta funcion solo es para la el adjusted close osea precio de ajuste de cierre
    df = pd.DataFrame(index=dates) #crear una matris donde las comlumnas son los indices y las fechas son los renglones
    if 'SPY' not in symbols:  # add SPY for reference, if absent
    #en la bolsa mexicana (BMV) el IPC seria el SPY
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        f = web.DataReader(symbol, 'google',dates[0],dates[-1]) #read from google
       # print(symbol)
       # print(f.tail())
        f=f.filter(items=['Close'])
        f=f.rename(columns={'Close':symbol})
        df=df.join(f)

        if symbol == 'SPY':
            df=df.dropna(subset=["SPY"])

    #print(df)
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2011', '2018')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    #print (df)
    print (df.head())
    print(df.tail())
    #print (df.loc['2017':'2018'])

    print("hello")
    data = [go.Scatter(x=df.index, y=df)]
    py.offline.plot(data)




if __name__ == "__main__":
    test_run()
