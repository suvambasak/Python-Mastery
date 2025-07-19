'''
1. https://docs.python.org/3/library/getpass.html
'''

import getpass
from enum import Enum

from shopping.product.policy import Policy
from shopping.product.policy_enums import ReplacementPolicy, WarrantyPolicy
from shopping.product.product import Product
from shopping.seller.seller_details import SellerDetails
from shopping.users.user import User
from shopping.orders.order_records import OrderRecord


class UserStates(Enum):
    HOME = 0
    USER_LOGIN = 1
    SELLER_LOGIN = 2


users: list[User] = []
seller_details: list[SellerDetails] = []
products: list[Product] = []
order_records: list[OrderRecord] = []

user_state: UserStates = UserStates.HOME
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
    global user_state

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
                user_state = UserStates.SELLER_LOGIN if user._is_seller else UserStates.USER_LOGIN
                return True
            else:
                break

    print('\nUser not found or invalid credentials')
    return False


def logout() -> bool:
    global user_session
    global user_state

    if user_session:
        _name = user_session._name
        user_session = None
        user_state = UserStates.HOME
        print(f'\n{_name} logged out successfully')
        return True

    print('\nNo user logged in')
    return False


def become_seller() -> bool:
    global user_session
    global user_state

    if not user_session:
        print('\nNo user logged in')
        return False

    user_id = users.index(user_session)
    GST_number = input('Enter your GST number: ')
    store_name = input('Enter your store name: ')
    pickup_address = input('Enter your pickup address: ')
    bank_account = input('Enter your bank account number: ')
    bank_ifsc = input('Enter your bank IFSC code: ')

    seller_details.append(SellerDetails(
        user_id=user_id,
        GST_number=GST_number,
        sore_name=store_name,
        pickup_address=pickup_address,
        bank_account_number=bank_account,
        bank_account_ifsc=bank_ifsc
    ))

    user_state = UserStates.SELLER_LOGIN
    user_session.set_seller()
    print('\nSeller details added successfully')
    return True


def add_product() -> bool:
    global user_session
    global user_state
    global products

    if not user_session:
        print('\nNo user logged in')
        return False
    if user_state != UserStates.SELLER_LOGIN:
        print('\nUser is not a seller')
        return False

    product_name = input('Enter product name: ')
    product_images_file = input('Enter product images file: ').split(',')

    print('Policy details')
    free_shipping = input('Free shipping (y/n): ')
    free_shipping = True if free_shipping == 'y' else False
    pay_on_delivery = input('Pay on delivery (y/n): ')
    pay_on_delivery = True if pay_on_delivery == 'y' else False

    for policy in [
        WarrantyPolicy.NO_WARRANTY,
        WarrantyPolicy.WARRANTY_WEEK,
        WarrantyPolicy.WARRANTY_MONTH,
        WarrantyPolicy.WARRANTY_YEAR
    ]:
        warranty_policy = input(f'{policy.name} (y/n): ')
        if warranty_policy == 'y':
            warranty_policy = policy
            break

    for policy in [
        ReplacementPolicy.NO_REPLACEMENT,
        ReplacementPolicy.REPLACEMENT_WEEK,
        ReplacementPolicy.REPLACEMENT_MONTH,
        ReplacementPolicy.REPLACEMENT_YEAR
    ]:
        replacement_policy = input(f'{policy.name} (y/n): ')
        if replacement_policy == 'y':
            replacement_policy = policy
            break

    maximum_retail_price = float(input('Enter maximum retail price: '))
    discount_percent = float(input('Enter discount percent: '))
    more_details = input('Enter more details: ').split(',')

    policy = Policy(
        free_shipping=free_shipping,
        pay_on_delivery=pay_on_delivery,
        warranty=warranty_policy,
        replacement=replacement_policy
    )
    product = Product(
        name=product_name,
        product_images_file=product_images_file,
        policy=policy,
        maximum_retail_price=maximum_retail_price,
        discount_percent=discount_percent
    )
    if more_details:
        more_details = {key: value for key, value in zip(
            more_details[::2], more_details[1::2])}
        product.add_more_details(more_details)

    products.append(product)

    print('\nProduct added successfully')
    return True


def explore_products() -> bool:
    global products
    global user_session
    global user_state

    if not user_session:
        print('\nNo user logged in')
        return False

    if user_state != UserStates.USER_LOGIN:
        print('\nUser is not a buyer')
        return False

    if not products:
        print('\nNo products available')
        return False

    print('\nAvailable products:')
    for idx, product in enumerate(products):
        print('____________________________________________________________', idx)
        product.show()
        print('____________________________________________________________')

    return True


def place_order() -> bool:
    global products
    global user_session
    global user_state

    if not user_session:
        print('\nNo user logged in')
        return False

    if user_state != UserStates.USER_LOGIN:
        print('\nUser is not a buyer')
        return False

    if not products:
        print('\nNo products available')
        return False

    product_id = int(input('Enter product ID to place order: '))
    if product_id < 0 or product_id >= len(products):
        print('\nInvalid product ID')
        return False

    order_record = OrderRecord(
        user_id=users.index(user_session),
        order_id=len(order_records),
        product_id=product_id
    )
    order_records.append(order_record)

    print(f'\nOrder placed successfully! Order ID: {order_record.order_id}')
    return True


def view_order_history() -> bool:
    global user_session
    global order_records

    if not user_session:
        print('\nNo user logged in')
        return False

    user_id = users.index(user_session)
    user_orders = [
        order for order in order_records if order.user_id == user_id]

    if not user_orders:
        print('\nNo orders found for this user')
        return False

    print('\nOrder History:')
    for idx, order in enumerate(user_orders):
        print('____________________________________________________________', idx+1)
        print(f'Order ID: {order.order_id}, Status: {order.status}')
        print(products[order.product_id].show())
        print('____________________________________________________________')

    return True


ROUTE = {
    '1': (
        create_user,
        'Create new user',
        {UserStates.HOME}
    ),
    '2': (
        login,
        'Login',
        {UserStates.HOME}
    ),
    '3': (
        logout,
        'Logout',
        {UserStates.USER_LOGIN, UserStates.SELLER_LOGIN}
    ),
    '4': (
        become_seller,
        'Become seller',
        {UserStates.USER_LOGIN}
    ),
    '5': (
        add_product,
        'Add product',
        {UserStates.SELLER_LOGIN}
    ),
    '6': (
        explore_products,
        'Explore products',
        {UserStates.USER_LOGIN}
    ),
    '7': (
        place_order,
        'Place order',
        {UserStates.USER_LOGIN}
    ),
    '8': (
        view_order_history,
        'View order history',
        {UserStates.USER_LOGIN}
    ),
    'q': (
        exit,
        'Exit',
        {UserStates.HOME, UserStates.USER_LOGIN, UserStates.SELLER_LOGIN}
    ),
}


if __name__ == '__main__':

    MAX_RETRY = 4
    retry = 0

    while True:
        print('________________________________________________________')
        print('________________________Shopping________________________')
        for key, value in ROUTE.items():
            if user_state in value[2]:
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
