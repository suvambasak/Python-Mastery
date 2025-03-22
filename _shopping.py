'''
1. https://docs.python.org/3/library/getpass.html
'''

import getpass

from shopping.users.user import User

users: list[User] = []


user_session: User | None = None


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
        print('\nNew user creation failed!')
        return False

    print(new_user)
    users.append(new_user)
    print('\nNew user created successfully!')
    return True


def login() -> bool:

    print('\nUser authentication')
    global user_session

    if user_session:
        print(f'{user_session._name} already logged in')
        return False

    _email = input('Enter your email: ')
    _password = getpass.getpass('Enter your password: ')

    for user in users:
        if user._email == _email:

            if user.authenticate(_password):
                print(f'\n{user._name} authenticated successfully')
                user_session = user
                return True
            else:
                break

    print('\nUser not found or invalid credentials')
    return False


def logout() -> bool:
    global user_session

    if user_session:
        _name = user_session._name
        user_session = None
        print(f'\n{_name} logged out successfully')
        return True

    print('\nNo user logged in')
    return False


ROUTE = {
    '1': (create_user, 'Create new user'),
    '2': (login, 'Login'),
    '3': (logout, 'Logout'),
    'q': (exit, 'Exit'),
}


if __name__ == '__main__':

    MAX_RETRY = 4
    retry = 0

    while True:
        print('________________________________________________________')
        print('________________________Shopping________________________')
        for key, value in ROUTE.items():
            print(f'{key}: {value[1]}')
        print('________________________________________________________')
        user_input = input('Enter your choice: ')

        if user_input in ROUTE:
            while not ROUTE[user_input][0]() and retry < MAX_RETRY:
                retry += 1
                print('Try again later')
                break
        else:
            print('Invalid choice')
