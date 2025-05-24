# lib/book.py

class Book:
    def __init__(self, title, page_count, price=0):
        self.title = title
        self._page_count = None
        self._price = None
        self.page_count = page_count  # use setter for validation
        self.price = price            # use setter for validation

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        self._price = value
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
