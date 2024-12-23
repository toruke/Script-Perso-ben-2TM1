import unittest

from Script.StockManager import StockManager


class TestStockManager(unittest.TestCase):
    def testInitialization(self):
        self.manager = StockManager()