import re

class User:
    def __init__(self, username: str, password: str, email: str):
        # Validate username
        if not (3 <= len(username) <= 20) or not username.isalnum() or username != username.strip():
            raise ValueError("Invalid username")

        # Validate password
        if len(password) < 8 or password.isspace() or not any(char.isdigit() for char in password) \
                or not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/`~' for char in password):
            raise ValueError("Invalid password")

        # Validate email
        email = email.strip()
        if len(email) > 254 or not re.match(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$", email):
            raise ValueError("Invalid email")

        self.username = username
        self.password = password
        self.email = email

    def update_email(self, new_email: str):
        new_email = new_email.strip()
        if len(new_email) > 254 or not re.match(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$", new_email):
            raise ValueError("Invalid email")
        self.email = new_email


class Product:
    def __init__(self, name: str, price: float, description: str):
        # Validate name
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        if not (1 <= len(name.strip()) <= 50):
            raise ValueError("Invalid product name")
        if name.strip() == '':
            raise ValueError("Invalid product name")

        # Validate price
        if not isinstance(price, (int, float)):
            raise TypeError("Product price must be a numeric value.")
        if not (price > 0 and price <= 10000.00):
            raise ValueError("Invalid product price")

        # Validate description
        if not isinstance(description, str):
            raise TypeError("Product description must be a string.")
        if len(description.strip()) > 200:
            raise ValueError("Description length exceeds 200 characters")

        self.name = name.strip()
        self.price = round(price, 6)  # Preserve up to 6 decimal places
        self.description = description.strip()


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product: Product, quantity: int):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 1 or quantity > 100:
            raise ValueError("Invalid quantity")

        for item in self.cart:
            if item['product'] == product:
                item['quantity'] += quantity
                return
        self.cart.append({'product': product, 'quantity': quantity})

    def view_cart(self):
        return self.cart.copy()


class Order:
    def __init__(self, user: User, items: list, address: str, payment_method: str):
        valid_payment_methods = ['credit_card', 'debit_card', 'paypal']

        if user is None:
            raise ValueError("User cannot be None.")
        if not items or any(item is None or item['quantity'] <= 0 for item in items):
            raise ValueError("Invalid order items.")
        address = address.strip()
        if not (1 <= len(address) <= 100) or any(ord(char) < 32 for char in address) or address.strip() == '':
            raise ValueError("Invalid address length or contains non-printable characters.")
        if payment_method not in valid_payment_methods:
            raise ValueError("Invalid payment method.")

        self.user = user
        self.items = items
        self.address = address
        self.payment_method = payment_method
        self.status = 'Processing'

    def update_status(self, new_status: str):
        valid_statuses = ['Processing', 'Shipped', 'Delivered', 'Cancelled']
        status_flow = {
            'Processing': ['Processing', 'Shipped', 'Cancelled'],
            'Shipped': ['Shipped', 'Delivered', 'Cancelled'],
            'Delivered': ['Delivered'],
            'Cancelled': ['Cancelled']
        }

        if new_status not in valid_statuses:
            raise ValueError("Invalid status")
        if new_status == self.status:
            return  # No change is needed if it's the same status
        if new_status not in status_flow[self.status]:
            raise ValueError(f"Cannot change status from {self.status} to {new_status}")
        self.status = new_status


class EcommerceApp:
    def __init__(self):
        self.users = {}
        self.products = []
        self.carts = {}
        self.orders = []

    def register_user(self, username: str, password: str, email: str) -> bool:
        if any(user.username.lower() == username.lower() for user in self.users.values()):
            raise ValueError("Username already exists")
        if any(user.email.lower() == email.lower() for user in self.users.values()):
            raise ValueError("Email already exists")

        new_user = User(username, password, email)
        self.users[username] = new_user
        self.carts[username] = ShoppingCart()
        return True

    def add_product(self, name: str, price: float, description: str) -> bool:
        new_product = Product(name, price, description)
        self.products.append(new_product)
        return True

    def add_to_cart(self, username: str, product_id: int, quantity: int) -> bool:
        if username not in self.users:
            raise ValueError("User not registered")
        if product_id < 0 or product_id >= len(self.products):
            raise ValueError("Invalid product ID")

        product = self.products[product_id]
        self.carts[username].add_to_cart(product, quantity)
        return True

    def checkout(self, username: str, address: str, payment_method: str) -> int:
        if username not in self.users or username not in self.carts or not self.carts[username].cart:
            raise ValueError("Cart is empty")

        new_order = Order(self.users[username], self.carts[username].view_cart(), address, payment_method)
        self.orders.append(new_order)
        self.carts[username] = ShoppingCart()  # Empty the cart after checkout
        return len(self.orders) - 1

    def track_order(self, order_id: int):
        if order_id < 0 or order_id >= len(self.orders):
            raise ValueError("Invalid order ID")
        return self.orders[order_id]
