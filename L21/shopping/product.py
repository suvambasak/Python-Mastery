

class Product:

    def __init__(self, name: str, maximum_retail_price: float, discount_percent: float = 0) -> None:
        self.name = name
        self.maximum_retail_price = maximum_retail_price
        self.discount_percent = discount_percent

    @property
    def price(self) -> int:
        return round(self.maximum_retail_price * (1 - self.discount_percent / 100))


if __name__ == '__main__':
    p1 = Product('Mossad', 450, 29)
    print(p1.__dict__)
    print(p1.price)
