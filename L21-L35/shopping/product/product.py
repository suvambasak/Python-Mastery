from shopping.product.policy import Policy


class Product:

    def __init__(
            self,
            name: str,
            product_images_file: list[str],
            policy: Policy,
            maximum_retail_price: float,
            discount_percent: float = 0,
    ) -> None:
        self._name = name
        self._product_images_file = product_images_file
        self._policy = policy
        self._maximum_retail_price = maximum_retail_price
        self._discount_percent = discount_percent
        self._more_details = {}

    @property
    def price(self) -> int:
        return round(self._maximum_retail_price * (1 - self._discount_percent / 100))

    def add_more_details(self, more_details: dict[str, str | int | float]) -> None:
        self._more_details = more_details

    def show(self) -> None:
        print(f'Name: {self._name}')
        print(f'Price: {self.price}')
        print(f'MRP: {self._maximum_retail_price}')
        print(f'Discount: {self._discount_percent}%')
        print(f'Images: {self._product_images_file}')
        print(f'Policy: {self._policy}')
        print('More details:')
        for key, value in self._more_details.items():
            print(f'\t{key}: {value}')
