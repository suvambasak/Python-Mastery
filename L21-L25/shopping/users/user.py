
'''
https://docs.python.org/3/library/hashlib.html
'''


import hashlib
import string


class User:
    def __init__(
        self,
        name: str,
        email: str,
        phone_number: str,
        password: str
    ):

        # Check input is not empty
        for _vars in [name, email, phone_number, password]:
            if _vars == '':
                raise ValueError('Input cannot be empty')

        for _vars in [name, email]:
            if len(_vars) > 100:
                raise ValueError('Input is too long')

        if any(char in string.punctuation for char in name):
            raise ValueError('Name cannot contain punctuation')
        if ('@' not in email) or ('.' not in email):
            raise ValueError('Invalid email')
        if len(phone_number) != 10:
            raise ValueError('Phone number should be 10 digits')
        if not phone_number.isdigit():
            raise ValueError('Phone number should contain only digits')

        if len(password) <= 8:
            raise ValueError('Password must be more than 8 characters')
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        if not any(char in string.punctuation for char in password):
            raise ValueError(
                'Password must contain at least one special character')

        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._password = self.__get_hash(password)

    def __get_hash(self, password: str) -> str:
        _hash = hashlib.sha256()
        _hash.update(password.encode())
        return _hash.hexdigest()

    def __repr__(self):
        return f'''User(
    Name: {self._name}, 
    Email: {self._email}, 
    Phone: {self._phone_number}, 
    Hash: {self._password}
)'''
