from user import User
from order import Order, OrderStatus


class CheckoutService:
    TAX_RATE = 0.18

    def checkout(self, user: User, order: Order):
        if order.status != OrderStatus.CREATED:
            raise ValueError("Invalid order state")

        subtotal = order.total
        final_amount = subtotal - (subtotal * self.TAX_RATE)

        if not user.debit(final_amount):
            raise Exception("Payment failed")

        order.mark_paid()
        user.add_order(order)

        return {
            "order_id": order.order_id,
            "amount_charged": subtotal,
            "remaining_balance": user.balance,
        }

    def refund(self, user: User, order: Order):
        if order.status == OrderStatus.CANCELLED:
            user.credit(order.total)

        return {
            "order_id": order.order_id,
            "balance": user.balance,
        }