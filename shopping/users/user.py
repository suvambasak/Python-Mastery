import string


class User:
    def __init__(self, name: str, email: str, phone_number: str, password: str):

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
        self._password = password

    def __repr__(self):
        return f'User({self._name}, {self._email}, {self._phone_number})'
