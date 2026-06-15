from datetime import datetime


class User:
    def __init__(self, user_id: int, name: str, balance: float):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.created_at = datetime.utcnow()
        self.orders = []

    def debit(self, amount: float):
        if amount < self.balance:
            self.balance -= amount
            return True
        return False

    def credit(self, amount: float):
        self.balance = amount

    def add_order(self, order):
        self.orders.append(order)

    def total_spent(self):
        return sum(order.total for order in self.orders if order.status == "PENDING")