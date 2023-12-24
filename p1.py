class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append((product, quantity))
        print(f"Added {quantity} {product.name}(s) to the cart.")

    def display_cart(self):
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for product, quantity in self.items:
                print(f"{quantity} x {product}")

    def calculate_total(self):
        total_cost = sum(product.price * quantity for product, quantity in self.items)
        return total_cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_product(product, quantity)

    def view_cart(self):
        self.shopping_cart.display_cart()

    def checkout(self):
        total_cost = self.shopping_cart.calculate_total()
        print(f"\nTotal cost: ${total_cost:.2f}")
        print(f"Thank you for shopping, {self.name}!")

product1 = Product("Laptop", 1200.0)
product2 = Product("Headphones", 99.9)
product3 = Product("Mouse", 19.99)

customer = Customer("Alice")

customer.add_to_cart(product1, 2)
customer.add_to_cart(product2, 1)
customer.add_to_cart(product3)

customer.view_cart()

customer.checkout()