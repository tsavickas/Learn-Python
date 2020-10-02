class Product:
    def __init__(self, price):
        self.price = price

    # property is an object that sit in front of an attribute and allows us to get or set value os an attribute
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(-10)
print(product.price)
