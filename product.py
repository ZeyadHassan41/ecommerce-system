class Product:
    def __init__(self, name, price, quantity, is_expired=False, weight=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_expired = is_expired
        self.weight = weight

    def is_shippable(self):
        return self.weight