class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        if product.quantity < quantity:
            raise ValueError(f"Not enough stock for {product.name}")
        if product.is_expired:
            raise ValueError(f"{product.name} is expired")
        self.items.append(CartItem(product, quantity))

    def is_empty(self):
        return len(self.items) == 0


