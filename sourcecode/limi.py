# limit_order_agent.py
class LimitOrderAgent:
    def __init__(self, execution_client):
        self.execution_client = execution_client
        self.orders = [] 
    
    def price_tick(self, product_id, price):
        if product_id == 'IBM' and price < 100:
            self.execution_client.execute_order('buy', product_id, 1000)
        for order in self.orders:
            if order['product_id'] == product_id:
                if order['side'] == 'buy' and price <= order['limit_price']:
                    self.execution_client.execute_order('buy', product_id, order['amount'])
                    self.orders.remove(order)
                elif order['side'] == 'sell' and price >= order['limit_price']:
                    self.execution_client.execute_order('sell', product_id, order['amount'])
                    self.orders.remove(order)

    def add_order(self, side, product_id, amount, limit_price):
        order = {
            'side': side,
            'product_id': product_id,
            'amount': amount,
            'limit_price': limit_price
        }
        self.orders.append(order)
