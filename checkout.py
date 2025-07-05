from cart import Cart
from customer import Customer
from shipping import ShippingService


class Checkout:
    def __init__(self, customer: Customer, cart: Cart):
        self.customer = customer
        self.cart = cart
        self.subtotal = 0
        self.shipping_fee = 0
        self.total = 0
        self.shippable_items = []

    def process(self):
        if self.cart.is_empty():
            raise Exception("Cart is empty")

        for item in self.cart.items:
            product = item.product
            quantity = item.quantity

            if product.quantity < quantity:
                raise Exception(f"Not enough stock for {product.name}")
            if product.is_expired:
                raise Exception(f"{product.name} is expired")

            self.subtotal += product.price * quantity

            if product.is_shippable():
                for _ in range(quantity):
                    self.shippable_items.append(product)

        if self.shippable_items:
            self.shipping_fee = ShippingService.ship(self.shippable_items)
        else:
            self.shipping_fee = 0
        self.total = self.subtotal + self.shipping_fee

        if self.customer.balance < self.total:
            raise Exception("Insufficient balance")

        self.customer.balance -= self.total

        if self.shippable_items:
            ShippingService.ship(self.shippable_items)

        self.print_receipt()

    def print_receipt(self):
        print("** Checkout receipt **")
        for item in self.cart.items:
            total_price = item.product.price * item.quantity
            print(f"{item.quantity}x {item.product.name}".ljust(20) + f"{total_price}")
        print("-" * 22)
        print(f"Subtotal\t\t" + f"{self.subtotal}")
        print(f"Shipping\t\t" + f"{self.shipping_fee}")
        print(f"Amount\t\t\t" + f"{self.total}")
        print(f"Remaining Balance:\t{self.customer.balance}")
