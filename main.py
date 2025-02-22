
from shopping.users.user import User


u1 = User('John Doe', 'jo@email.com', '9051446080', 'password@123')

print(u1)


# from shopping.product.policy_enums import WarrantyPolicy, ReplacementPolicy
# from shopping.product.policy import Policy
# from shopping.product.product import Product

# p1 = Product(
#     name='Mossad',
#     product_images_file=['path/to/image1.jpg',
#                          'path/to/image2.jpg', 'path/to/image3.jpg'],
#     policy=Policy(
#         True,
#         True,
#         WarrantyPolicy.WARRANTY_YEAR,
#         ReplacementPolicy.REPLACEMENT_MONTH
#     ),
#     maximum_retail_price=450,
#     discount_percent=29
# )
# p1.add_more_details({
#     'author': 'Michael Bar-Zohar',
#     'genre': 'Non-fiction',
#     'publisher': 'HarperCollins'
# })

# p1.show()
