'''
1. https://docs.python.org/3/library/getpass.html
'''

import getpass

from shopping.users.user import User

users: list[User] = []


def create_user() -> bool:
    print('\nCreating new user')

    _name = input('Enter your name: ')
    _email = input('Enter your email: ')
    _phone_num = input('Enter your phone number: ')
    _password = getpass.getpass('Enter your password: ')

    try:
        new_user = User(
            name=_name,
            email=_email,
            phone_number=_phone_num,
            password=_password
        )
        print(new_user)
        new_user.verify_user()
    except ValueError as e:
        print(e)
        return False

    print(new_user)
    users.append(new_user)
    return True


# def login():
#     print('User login method to be created')


# def logout():
#     print('User logout method to be created')


ROUTE = {
    '1': (create_user, 'Create new user'),
    # '2': (login, 'Login'),
    # '3': (logout, 'Logout'),
    'q': (exit, 'Exit'),
}


if __name__ == '__main__':

    while True:
        print('________________________________________________________')
        print('________________________Shopping________________________')
        for key, value in ROUTE.items():
            print(f'{key}: {value[1]}')
        print('________________________________________________________')
        user_input = input('Enter your choice: ')

        if user_input in ROUTE:
            while not ROUTE[user_input][0]():
                pass
        else:
            print('Invalid choice')
