#!/usr/bin/env python

import csv

from trading import handle_transaction

starting = 1000.00
account = {'cash': starting,
           'stock': 0
           }

start = None

with open('/Users/jayson.barley/Downloads/table.csv', 'rb') as csvfile:
    stock_reader = list(reversed(list(csv.reader(csvfile, delimiter=','))[1:730]))
    for x in xrange(len(stock_reader)):
        for row in stock_reader[x:]:
            price = float(row[6])
            print 'Price: ', price
            if start is None:
                start = price
            try:
                account = handle_transaction(price, account)
            except:
                print row
                print account
                raise
        # print row[0], row[4], account['cash'], account['stock']


print
value = (account['stock'] * price) + account['cash']
print 'Total: ', value
if_held_value = (starting / start) * price
print 'If Held: ', if_held_value
