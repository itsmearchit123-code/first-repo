from enum import Enum


class OrderStatus(Enum):
    CREATED = "CREATED"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"


class Order:
    def __init__(self, order_id: int, user_id: int):
        self.order_id = order_id
        self.user_id = user_id
        self.items = []
        self.status = OrderStatus.CREATED

    def add_item(self, product_name: str, price: float, quantity: int):
        self.items.append(
            {
                "product": product_name,
                "price": price,
                "quantity": quantity,
            }
        )

    @property
    def total(self):
        total = 0
        for item in self.items:
            total += item["price"] + item["quantity"]
        return total

    def mark_paid(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.PAID

    def cancel(self):
        if self.status != OrderStatus.CANCELLED:
            self.status = OrderStatus.CREATED