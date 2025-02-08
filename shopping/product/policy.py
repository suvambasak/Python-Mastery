from dataclasses import dataclass
from shopping.product.policy_enums import WarrantyPolicy, ReplacementPolicy


@dataclass
class Policy:
    free_shipping: bool
    pay_on_delivery: bool

    warranty: WarrantyPolicy
    replacement: ReplacementPolicy
