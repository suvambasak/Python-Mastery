from dataclasses import dataclass


@dataclass
class OrderRecord:
    order_id: int
    user_id: int
    product_id: int
    status: str = 'Placed'
