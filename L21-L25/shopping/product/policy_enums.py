from enum import Enum


class WarrantyPolicy(Enum):
    NO_WARRANTY = 0
    WARRANTY_WEEK = 1
    WARRANTY_MONTH = 2
    WARRANTY_YEAR = 3


class ReplacementPolicy(Enum):
    NO_REPLACEMENT = 0
    REPLACEMENT_WEEK = 1
    REPLACEMENT_MONTH = 2
    REPLACEMENT_YEAR = 3
