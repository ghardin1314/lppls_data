# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:10:38 2019

@author: Garrett

initializes database to store data. Will be called in main script if database
does not exist. Might have to turn it into a function. 
"""


import sqlite3

conn = sqlite3.connect('lppls_data.db')

c = conn.cursor()

c.execute("""CREATE TABLE lppls_scores (
        stock_name text,
        sector text,
        date text,
        price real,
        bubble_start text,
        days_out integer,
        bubble_per real,
        bubble_size real,
        agg_score real,
        mu_per real,
        std_dev real,
        IV_per real)""")

conn.commit()