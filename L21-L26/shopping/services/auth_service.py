
from abc import ABC, abstractmethod
import string
import random


class OTPService(ABC):
    def __init__(self, user_id: str):
        self._user_id = user_id

    def generate_verification_code(self):
        self.__verification_code = ''.join(
            random.choices(string.digits, k=6)
        )
        print(f'Verification code: {self.__verification_code}')

    @abstractmethod
    def send_verification_code(self):
        pass

    def verify_code(self, code: str):
        return code == self.__verification_code


class EmailOTPService(OTPService):
    def send_verification_code(self):
        print(
            f'''Sending verification code to {self._user_id}'''
        )


class PhoneOTPService(OTPService):
    def send_verification_code(self):
        print(
            f'''Sending verification code to {self._user_id}'''
        )
