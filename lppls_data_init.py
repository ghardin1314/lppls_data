# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:10:38 2019

@author: Garrett
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
        mu_per real,
        std_dev real,
        agg_score real,
        IV_per real)
        """)

conn.commit()