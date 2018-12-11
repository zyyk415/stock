#!/usr/bin/python
#coding=UTF-8
import tushare as ts
import os
import threading

def get_price():
    df = ts.get_realtime_quotes('002236') #Single stock symbol
    print(df[['name','price','time']])
    df = ts.get_realtime_quotes('002415') #Single stock symbol
    print(df[['name','price','time']])
    df = ts.get_realtime_quotes('000651') #Single stock symbol
    print(df[['name','price','time']])
    df = ts.get_realtime_quotes('000002') #Single stock symbol
    print(df[['name','price','time']])
    timer = threading.Timer(30,get_price)  #首次启动
    timer.start() 

timer = threading.Timer(1,get_price)  #首次启动
timer.start() 
