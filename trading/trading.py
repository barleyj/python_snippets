#!/usr/bin/env python

import unittest


stock_distribution = .75


def handle_transaction(price, account):
    global stock_distribution

    stock_value = price * account['stock']
    current_distribution = stock_value / (account['cash'] + stock_value)
    desired = (stock_value + account['cash']) * stock_distribution

    if current_distribution < stock_distribution:
        stock_to_purchase = int(desired / price) - account['stock']
        print 'Stock to purchase: ', stock_to_purchase
        account = {'cash': account['cash'] - (stock_to_purchase * price),
                   'stock': account['stock'] + stock_to_purchase
                   }
    if current_distribution > stock_distribution:
        stock_to_sell = account['stock'] - int(desired / price)
        print 'Stock to sell: ', stock_to_sell
        account = {'cash': account['cash'] + (stock_to_sell * price),
                   'stock': account['stock'] - stock_to_sell
                   }

    return account


class TestHandleTransaction(unittest.TestCase):
    def test_purchase(self):
        account = {'cash': 1000.00,
                   'stock': 0
                   }

        result = handle_transaction(price, account)

        self.assertTrue(result['cash'], 250.00)
        self.assertTrue(result['stock'], 150)

    def test_sell(self):
        account = {'cash': 0.00,
                   'stock': 200
                   }

        result = handle_transaction(price, account)

        self.assertEqual(result['cash'], 250.00)
        self.assertEqual(result['stock'], 150)

    def test_buy_rebalance(self):
        account = {'cash': 500.00,
                   'stock': 100
                   }

        result = handle_transaction(price, account)

        self.assertEqual(result['cash'], 250.00)
        self.assertEqual(result['stock'], 150)

    def test_sell_rebalance(self):
        account = {'cash': 125.00,
                   'stock': 175
                   }

        result = handle_transaction(price, account)

        self.assertEqual(result['cash'], 250.00)
        self.assertEqual(result['stock'], 150)


if __name__ == '__main__':
    unittest.main()
