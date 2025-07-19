from enum import Enum


class UserStatus(Enum):
    ACTIVE = 0
    BLOCKED = 1

    UNVERIFIED = 2
    ONLY_EMAIL_VERIFIED = 3
    ONLY_PHONE_VERIFIED = 4
