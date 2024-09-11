
import unittest

from limi import LimitOrderAgent

class MockExecutionClient:
    def __init__(self):
        self.executed_orders = []

    def execute_order(self, side, product_id, amount):
        self.executed_orders.append((side, product_id, amount))


class TestLimitOrderAgent(unittest.TestCase):
    def setUp(self):
        self.execution_client = MockExecutionClient()
        self.agent = LimitOrderAgent(self.execution_client)

    def test_buy_ibm_below_100(self):
        self.agent.price_tick('IBM', 99)
        self.assertIn(('buy', 'IBM', 1000), self.execution_client.executed_orders)

    def test_add_and_execute_buy_order(self):
        self.agent.add_order('buy', 'AAPL', 500, 150)
        self.agent.price_tick('AAPL', 149)
        self.assertIn(('buy', 'AAPL', 500), self.execution_client.executed_orders)

    def test_add_and_execute_sell_order(self):
        self.agent.add_order('sell', 'GOOGL', 200, 2000)
        self.agent.price_tick('GOOGL', 2001)
        self.assertIn(('sell', 'GOOGL', 200), self.execution_client.executed_orders)

if __name__ == '__main__':
    unittest.main()
