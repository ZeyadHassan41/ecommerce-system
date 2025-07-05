from cart import Cart
from customer import Customer
from product import Product
from checkout import Checkout

def main():
    cheese = Product("Cheese", 100, 10, is_expired=False, weight=200)
    biscuits = Product("Biscuits", 150, 5, is_expired=False, weight=700)
    tv = Product("TV", 4000, 2, is_expired=False, weight=10000)
    scratch_card = Product("Mobile scratch card", 50, 100, is_expired=False)

    customer = Customer("Zeyad", balance=1000)

    cart = Cart()
    cart.add(cheese, 2)
    cart.add(biscuits, 1)
    cart.add(scratch_card, 1)

    checkout = Checkout(customer, cart)
    checkout.process()

if __name__ == "__main__":
    main()
