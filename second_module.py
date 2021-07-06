from decimal import Decimal
import json


class Order:
    def __init__(self, price: Decimal, lots: int) -> None:
        if not isinstance(price, Decimal):
            raise ValueError("Price must be Decmial!")

        self.price = price
        self.lots = lots

    def get_price(self) -> Decimal:
        """Return order's price."""
        return self.price

    def get_lots(self) -> int:
        """Return order's lots count."""
        return self.lots


def serialize_order(order: Order) -> str:
    """Conver Order to json string."""
    order_dict = order.__dict__
    order_dict['price'] = str(order_dict['price'])
    return json.dumps(order_dict)


def unserialize_order(serialized_order: str) -> Order:
    """Convert json string order to class Order."""
    serialized_order = json.loads(serialized_order)

    lots = int(serialized_order["lots"])
    price = Decimal(serialized_order["price"])
    return Order(price, lots)
