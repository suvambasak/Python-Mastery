

from dataclasses import dataclass


@dataclass
class SellerDetails:
    user_id: int

    GST_number: str
    sore_name: str
    pickup_address: str
    bank_account_number: str
    bank_account_ifsc: str
