class Shoe:
    def __init__(self, brand, size, price=0):
        self.brand = brand
        self._size = None
        self._price = None
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        self._price = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
