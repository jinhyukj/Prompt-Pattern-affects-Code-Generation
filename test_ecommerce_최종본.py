import pytest
from complete_code import User, Product, ShoppingCart, Order, EcommerceApp

########################
### class User Tests ###
########################

def test_user_creation_valid_case_1():
    # General Case 1: Create a user with typical valid username, password, and email
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    assert user.username == 'johndoe'
    assert user.password == 'Password123!'
    assert user.email == 'johndoe@example.com'

def test_user_creation_valid_case_2():
    # General Case 2: Create a user with a different valid username, password, and email format
    user = User('janedoe', 'SecurePass!9', 'jane.doe@sub.domain.com')
    assert user.username == 'janedoe'
    assert user.password == 'SecurePass!9'
    assert user.email == 'jane.doe@sub.domain.com'

def test_user_creation_valid_case_3():
    # General Case 3: Create a user with mixed-case username and valid password and email
    user = User('JohnDoe', 'Another$Pass1', 'john.doe@domain.co.uk')
    assert user.username == 'JohnDoe'
    assert user.password == 'Another$Pass1'
    assert user.email == 'john.doe@domain.co.uk'

# Username Edge Cases:
# Length is exactly 3 or 20 characters:

def test_user_creation_username_exact_length():
    # Edge Case: Username with exactly 3 characters (valid)
    user1 = User('abc', 'Password123!', 'abc@example.com')
    assert user1.username == 'abc'
    
    # Edge Case: Username with exactly 20 characters (valid)
    user2 = User('a' * 20, 'Password123!', 'user20chars@example.com')
    assert user2.username == 'a' * 20
# Contains special characters (invalid):

def test_user_creation_username_special_characters():
    # Edge Case: Username with special characters (invalid)
    with pytest.raises(ValueError, match="Invalid username"):
        User('user@name', 'Password123!', 'user@example.com')
# Contains leading or trailing spaces (invalid):

def test_user_creation_username_with_spaces():
    # Edge Case: Username with leading spaces (invalid)
    with pytest.raises(ValueError, match="Invalid username"):
        User(' user', 'Password123!', 'user@example.com')
    
    # Edge Case: Username with trailing spaces (invalid)
    with pytest.raises(ValueError, match="Invalid username"):
        User('user ', 'Password123!', 'user@example.com')
# Contains mixed case (e.g., "User" vs "user"):

def test_user_creation_username_mixed_case():
    # Edge Case: Username with mixed case
    user = User('UserMixed', 'Password123!', 'usermixed@example.com')
    assert user.username == 'UserMixed'
# Duplicate username:

def test_user_creation_duplicate_username():
    # Edge Case: Duplicate username (invalid)
    user1 = User('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Username already exists"):
        User('johndoe', 'AnotherPass1!', 'johndifferent@example.com')
# Password Edge Cases:
# Length is exactly 8 characters:
def test_user_creation_password_exact_length():
    # Edge Case: Password with exactly 8 characters (valid)
    user = User('johndoe', 'Pass12!@', 'johndoe@example.com')
    assert user.password == 'Pass12!@'
# Contains only spaces (invalid):

def test_user_creation_password_only_spaces():
    # Edge Case: Password with only spaces (invalid)
    with pytest.raises(ValueError, match="Invalid password"):
        User('johndoe', ' ' * 8, 'johndoe@example.com')
# Includes spaces (valid):

def test_user_creation_password_with_spaces():
    # Edge Case: Password with spaces (valid)
    user = User('janedoe', 'Pass word1!', 'janedoe@example.com')
    assert user.password == 'Pass word1!'
# Lacks special characters or numbers (invalid):

def test_user_creation_password_no_special_chars_or_numbers():
    # Edge Case: Password without special characters or numbers (invalid)
    with pytest.raises(ValueError, match="Invalid password"):
        User('janedoe', 'Password', 'janedoe@example.com')
# Includes special characters at various positions (valid):

def test_user_creation_password_special_chars_various_positions():
    # Edge Case: Password with special characters at various positions (valid)
    user = User('janedoe', '!Passw0rd!', 'janedoe@example.com')
    assert user.password == '!Passw0rd!'
# Email Edge Cases:
# Valid formats include subdomains and different TLDs:

def test_user_creation_email_valid_formats():
    # Edge Case: Email with subdomains (valid)
    user1 = User('janedoe', 'Password123!', 'user@sub.domain.com')
    assert user1.email == 'user@sub.domain.com'
    
    # Edge Case: Email with different TLD (valid)
    user2 = User('jackdoe', 'Password123!', 'user@domain.co.uk')
    assert user2.email == 'user@domain.co.uk'
# Invalid formats include missing '@', missing domain, invalid characters, or spaces:

def test_user_creation_email_invalid_formats():
    # Edge Case: Email missing '@' (invalid)
    with pytest.raises(ValueError, match="Invalid email"):
        User('janedoe', 'Password123!', 'userdomain.com')
    
    # Edge Case: Email missing domain (invalid)
    with pytest.raises(ValueError, match="Invalid email"):
        User('janedoe', 'Password123!', 'user@.com')
    
    # Edge Case: Email with invalid characters (invalid)
    with pytest.raises(ValueError, match="Invalid email"):
        User('janedoe', 'Password123!', 'user@domain$.com')
    
    # Edge Case: Email with spaces (invalid)
    with pytest.raises(ValueError, match="Invalid email"):
        User('janedoe', 'Password123!', ' user@domain.com ')
# Very long email addresses (up to 254 characters):

def test_user_creation_email_very_long():
    # Edge Case: Very long email address (valid)
    long_email = 'user' + 'a' * 240 + '@example.com'
    user = User('janedoe', 'Password123!', long_email)
    assert user.email == long_email
# Leading or trailing spaces (to be removed):
def test_user_creation_email_with_spaces():
    # Edge Case: Email with leading spaces
    user1 = User('janedoe', 'Password123!', ' user@domain.com')
    assert user1.email == 'user@domain.com'
    
    # Edge Case: Email with trailing spaces
    user2 = User('janedoe', 'Password123!', 'user@domain.com ')
    assert user2.email == 'user@domain.com'
# Duplicate email:

def test_user_creation_duplicate_email():
    # Edge Case: Duplicate email (invalid)
    user1 = User('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Email already exists"):
        User('janedoe', 'Password123!', 'johndoe@example.com')
# Mixed case (e.g., "User@domain.com" vs "user@domain.com"):

def test_user_creation_email_mixed_case():
    # Edge Case: Mixed-case email (valid)
    user1 = User('johndoe', 'Password123!', 'User@domain.com')
    user2 = User('janedoe', 'Password123!', 'user@domain.com')
    assert user1.email.lower() == user2.email.lower()

# Edge Cases for update_email(new_email: str) Method:
# Valid email formats as described above:

def test_update_email_valid_formats():
    # Edge Case: Update email with valid subdomain format
    user = User('janedoe', 'Password123!', 'janedoe@example.com')
    user.update_email('user@sub.domain.com')
    assert user.email == 'user@sub.domain.com'

    # Edge Case: Update email with different TLD format
    user.update_email('user@domain.co.uk')
    assert user.email == 'user@domain.co.uk'
# Invalid email formats as described above:

def test_update_email_invalid_formats():
    # Edge Case: Update email with missing '@' (invalid)
    user = User('janedoe', 'Password123!', 'janedoe@example.com')
    with pytest.raises(ValueError, match="Invalid email"):
        user.update_email('userdomain.com')

    # Edge Case: Update email with missing domain (invalid)
    with pytest.raises(ValueError, match="Invalid email"):
        user.update_email('user@.com')

    # Edge Case: Update email with invalid characters (invalid)
    with pytest.raises(ValueError, match="Invalid email"):
        user.update_email('user@domain$.com')

    # Edge Case: Update email with spaces (invalid)
    with pytest.raises(ValueError, match="Invalid email"):
        user.update_email(' user@domain.com ')
# Very long email addresses (up to 254 characters):

def test_update_email_very_long():
    # Edge Case: Update email with very long email address (valid)
    user = User('janedoe', 'Password123!', 'janedoe@example.com')
    long_email = 'user' + 'a' * 240 + '@example.com'
    user.update_email(long_email)
    assert user.email == long_email
# Leading or trailing spaces (to be removed):
def test_update_email_with_spaces():
    # Edge Case: Update email with leading spaces
    user = User('janedoe', 'Password123!', 'janedoe@example.com')
    user.update_email(' user@domain.com')
    assert user.email == 'user@domain.com'
    
    # Edge Case: Update email with trailing spaces
    user.update_email('user@domain.com ')
    assert user.email == 'user@domain.com'
# Duplicate email:

def test_update_email_duplicate_email():
    # Edge Case: Update email to a duplicate (invalid)
    user1 = User('johndoe', 'Password123!', 'johndoe@example.com')
    user2 = User('janedoe', 'Password123!', 'janedoe@example.com')
    with pytest.raises(ValueError, match="Email already exists"):
        user2.update_email('johndoe@example.com')
# Mixed case (e.g., "User@domain.com" vs "user@domain.com"):

def test_update_email_mixed_case():
    # Edge Case: Update email with mixed case (valid)
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    user.update_email('User@Domain.com')
    assert user.email == 'User@Domain.com'






############################
### class Product Tests ###
############################


def test_product_creation_with_valid_data():
    # General Case 1: Valid product creation with standard input
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    assert product.name == 'Laptop'
    assert product.price == 999.99
    assert product.description == 'A high-performance laptop'

def test_product_creation_minimum_valid_price():
    # General Case 2: Product creation with the minimum valid price
    product = Product('Mouse', 0.01, 'A basic computer mouse')
    assert product.name == 'Mouse'
    assert product.price == 0.01
    assert product.description == 'A basic computer mouse'

def test_product_creation_maximum_valid_price():
    # General Case 3: Product creation with the maximum valid price
    product = Product('Premium Laptop', 10000.00, 'A high-end premium laptop')
    assert product.name == 'Premium Laptop'
    assert product.price == 10000.00
    assert product.description == 'A high-end premium laptop'


# Edge Cases for name

def test_product_name_length_1_character():
    # Edge Case: Name with exactly 1 character
    product = Product('A', 50.0, 'A simple product with a short name.')
    assert product.name == 'A'

def test_product_name_length_50_characters():
    # Edge Case: Name with exactly 50 characters
    long_name = 'A' * 50
    product = Product(long_name, 50.0, 'A simple product with a long name.')
    assert product.name == long_name

def test_product_name_length_0_characters():
    # Edge Case: Name with 0 characters (invalid)
    with pytest.raises(ValueError, match="Invalid product name"):
        Product('', 50.0, 'A product with no name.')

def test_product_name_length_51_characters():
    # Edge Case: Name with 51 characters (invalid)
    long_name = 'A' * 51
    with pytest.raises(ValueError, match="Invalid product name"):
        Product(long_name, 50.0, 'A product with an overly long name.')

def test_product_name_with_special_characters():
    # Edge Case: Name with special characters
    product = Product('Laptop@2024!', 999.99, 'A laptop with special characters in its name.')
    assert product.name == 'Laptop@2024!'

def test_product_name_with_only_spaces():
    # Edge Case: Name with only spaces (invalid)
    with pytest.raises(ValueError, match="Invalid product name"):
        Product('   ', 50.0, 'A product with a name containing only spaces.')

def test_product_name_with_leading_trailing_spaces():
    # Edge Case: Name with leading or trailing spaces
    product = Product('  Tablet  ', 50.0, 'A product with spaces around the name.')
    assert product.name == 'Tablet'

def test_product_name_with_unicode_characters():
    # Edge Case: Name with Unicode characters
    product = Product('产品', 50.0, 'A product name in Chinese characters.')
    assert product.name == '产品'

def test_product_name_with_non_string_values():
    # Edge Case: Non-string name (invalid)
    with pytest.raises(TypeError):
        Product(1234, 50.0, 'A product with a non-string name.')
# Edge Cases for price

def test_product_price_minimum_value():
    # Edge Case: Price at the minimum valid value
    product = Product('Basic Mouse', 0.01, 'A basic computer mouse.')
    assert product.price == 0.01

def test_product_price_maximum_value():
    # Edge Case: Price at the maximum valid value
    product = Product('Luxury Watch', 10000.00, 'An extremely expensive watch.')
    assert product.price == 10000.00

def test_product_price_below_minimum_value():
    # Edge Case: Price below the minimum value (invalid)
    with pytest.raises(ValueError, match="Invalid product price"):
        Product('Cheap Mouse', 0.00, 'A product with an invalid price below the minimum.')

def test_product_price_above_maximum_value():
    # Edge Case: Price above the maximum value (invalid)
    with pytest.raises(ValueError, match="Invalid product price"):
        Product('Expensive TV', 10000.01, 'A product with an invalid price above the maximum.')

def test_product_price_negative_value():
    # Edge Case: Negative price (invalid)
    with pytest.raises(ValueError, match="Invalid product price"):
        Product('Negative Priced Product', -999.99, 'A product with a negative price.')

def test_product_price_very_small_decimals():
    # Edge Case: Price with very small decimals
    product = Product('Tiny Price Product', 0.001, 'A product with a very small decimal price.')
    assert product.price == 0.001

def test_product_price_very_large_decimals():
    # Edge Case: Price with very large decimals
    product = Product('Product with Large Decimals', 999.999999, 'A product priced with large decimals.')
    assert product.price == 999.999999

def test_product_price_many_decimal_places():
    # Edge Case: Price with a large number of decimal places
    product = Product('High Precision Product', 1234.567890123, 'A product with a high precision price.')
    assert round(product.price, 6) == 1234.567890

def test_product_price_non_numeric_value():
    # Edge Case: Non-numeric price (invalid)
    with pytest.raises(TypeError):
        Product('Invalid Price Product', 'not_a_price', 'A product with a non-numeric price.')
# Edge Cases for description

def test_product_description_length_0_characters():
    # Edge Case: Description with exactly 0 characters
    product = Product('No Description Product', 100.0, '')
    assert product.description == ''

def test_product_description_length_200_characters():
    # Edge Case: Description with exactly 200 characters
    long_description = 'A' * 200
    product = Product('Detailed Product', 100.0, long_description)
    assert product.description == long_description

def test_product_description_length_201_characters():
    # Edge Case: Description with 201 characters (invalid)
    long_description = 'A' * 201
    with pytest.raises(ValueError, match="Invalid product description"):
        Product('Overly Detailed Product', 100.0, long_description)

def test_product_description_with_special_characters_and_emojis():
    # Edge Case: Description with special characters and emojis
    product = Product('Emoji Product', 100.0, 'This product is amazing! 🤖✨🚀')
    assert product.description == 'This product is amazing! 🤖✨🚀'

def test_product_description_with_only_spaces():
    # Edge Case: Description with only spaces
    product = Product('Spaces Description Product', 100.0, '   ')
    assert product.description == ''

def test_product_description_with_leading_trailing_spaces():
    # Edge Case: Description with leading or trailing spaces
    product = Product('Trimmed Description Product', 100.0, '   A trimmed description.   ')
    assert product.description == 'A trimmed description.'

def test_product_description_with_non_string_values():
    # Edge Case: Non-string description (invalid)
    with pytest.raises(TypeError):
        Product('Invalid Description Product', 100.0, 1234)


###################################
### class ShoppingCart Tests ###
###################################


def test_add_single_product_to_cart():
    """
    General Case: Adding a single product to the shopping cart.
    """
    cart = ShoppingCart()
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    
    cart.add_to_cart(product, 1)  # Add 1 Laptop to the cart
    
    cart_contents = cart.view_cart()
    assert len(cart_contents) == 1
    assert cart_contents[0]['product'] == product
    assert cart_contents[0]['quantity'] == 1

def test_add_multiple_different_products_to_cart():
    """
    General Case: Adding multiple different products to the shopping cart.
    """
    cart = ShoppingCart()
    product1 = Product('Laptop', 999.99, 'A high-performance laptop')
    product2 = Product('Smartphone', 499.99, 'A high-end smartphone')
    
    cart.add_to_cart(product1, 2)  # Add 2 Laptops to the cart
    cart.add_to_cart(product2, 1)  # Add 1 Smartphone to the cart
    
    cart_contents = cart.view_cart()
    assert len(cart_contents) == 2
    assert cart_contents[0]['product'] == product1
    assert cart_contents[0]['quantity'] == 2
    assert cart_contents[1]['product'] == product2
    assert cart_contents[1]['quantity'] == 1

def test_update_quantity_of_existing_product_in_cart():
    """
    General Case: Updating the quantity of an existing product in the shopping cart.
    """
    cart = ShoppingCart()
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    
    cart.add_to_cart(product, 1)  # Add 1 Laptop to the cart
    cart.add_to_cart(product, 3)  # Add 3 more Laptops to the cart, should update the quantity to 4
    
    cart_contents = cart.view_cart()
    assert len(cart_contents) == 1
    assert cart_contents[0]['product'] == product
    assert cart_contents[0]['quantity'] == 4

# Edge Test Cases for add_to_cart Method

# Boundary Values

def test_add_product_quantity_lower_boundary():
    """
    Edge Case: Quantity is exactly 1 (lower boundary).
    """
    cart = ShoppingCart()
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    
    cart.add_to_cart(product, 1)  # Add 1 Laptop to the cart
    
    cart_contents = cart.view_cart()
    assert len(cart_contents) == 1
    assert cart_contents[0]['product'] == product
    assert cart_contents[0]['quantity'] == 1

def test_add_product_quantity_upper_boundary():
    """
    Edge Case: Quantity is exactly 100 (upper boundary).
    """
    cart = ShoppingCart()
    product = Product('Smartphone', 499.99, 'A high-end smartphone')
    
    cart.add_to_cart(product, 100)  # Add 100 Smartphones to the cart
    
    cart_contents = cart.view_cart()
    assert len(cart_contents) == 1
    assert cart_contents[0]['product'] == product
    assert cart_contents[0]['quantity'] == 100

# Invalid Quantity

def test_add_product_quantity_less_than_1():
    """
    Edge Case: Adding a product with quantity less than 1 (invalid).
    """
    cart = ShoppingCart()
    product = Product('Tablet', 299.99, 'A lightweight tablet')
    
    with pytest.raises(ValueError, match="Invalid quantity"):
        cart.add_to_cart(product, -1)  # Invalid quantity less than 1

def test_add_product_quantity_more_than_100():
    """
    Edge Case: Adding a product with quantity more than 100 (invalid).
    """
    cart = ShoppingCart()
    product = Product('Headphones', 79.99, 'Noise-cancelling headphones')
    
    with pytest.raises(ValueError, match="Invalid quantity"):
        cart.add_to_cart(product, 101)  # Invalid quantity more than 100

def test_add_product_quantity_zero():
    """
    Edge Case: Adding a product with quantity 0 (invalid).
    """
    cart = ShoppingCart()
    product = Product('Monitor', 199.99, 'A 24-inch LED monitor')
    
    with pytest.raises(ValueError, match="Invalid quantity"):
        cart.add_to_cart(product, 0)  # Invalid quantity of 0

def test_add_product_negative_quantity():
    """
    Edge Case: Adding a product with a negative quantity (invalid).
    """
    cart = ShoppingCart()
    product = Product('Keyboard', 49.99, 'Mechanical keyboard')
    
    with pytest.raises(ValueError, match="Invalid quantity"):
        cart.add_to_cart(product, -5)  # Negative quantity

def test_add_product_non_integer_quantity():
    """
    Edge Case: Adding a product with a non-integer quantity (e.g., 1.5 or "two") (invalid).
    """
    cart = ShoppingCart()
    product = Product('Mouse', 19.99, 'Wireless mouse')
    
    with pytest.raises(TypeError, match="Quantity must be an integer"):
        cart.add_to_cart(product, 1.5)  # Non-integer quantity

    with pytest.raises(TypeError, match="Quantity must be an integer"):
        cart.add_to_cart(product, "two")  # Non-integer quantity

# Adding the Same Product Multiple Times

def test_add_same_product_multiple_times():
    """
    Edge Case: Adding the same product multiple times should combine quantities or update the existing quantity.
    """
    cart = ShoppingCart()
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    
    cart.add_to_cart(product, 1)  # Add 1 Laptop to the cart
    cart.add_to_cart(product, 2)  # Add 2 more Laptops to the cart, should combine to 3
    
    cart_contents = cart.view_cart()
    assert len(cart_contents) == 1
    assert cart_contents[0]['product'] == product
    assert cart_contents[0]['quantity'] == 3

# Edge Test Cases for view_cart() Method
def test_view_empty_cart():
    """
    Edge Case: Viewing an empty cart should return an empty list.
    """
    cart = ShoppingCart()  # Create an empty shopping cart
    cart_contents = cart.view_cart()  # View the contents of the cart

    assert cart_contents == []  # Assert that the cart is empty


def test_view_cart_immutable_return():
    """
    Edge Case: Ensuring that the list returned by view_cart() does not allow modifications that affect the internal state of the cart.
    """
    cart = ShoppingCart()  # Create a shopping cart
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    
    cart.add_to_cart(product, 2)  # Add a product to the cart
    
    # View the contents of the cart
    cart_contents = cart.view_cart()
    
    # Try modifying the returned list (this should not affect the internal state of the cart)
    cart_contents.append({'product': product, 'quantity': 1})
    
    # View the cart again to verify its state has not been altered
    updated_cart_contents = cart.view_cart()
    
    # Assert the internal cart was not modified
    assert len(updated_cart_contents) == 1
    assert updated_cart_contents[0]['product'] == product
    assert updated_cart_contents[0]['quantity'] == 2


##########################
### class Order Tests ###
##########################
def test_order_initialization_valid():
    """
    General Case: Initialize an order with valid parameters.
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 2}]
    order = Order(user, items, '123 Main St', 'credit_card')
    
    assert order.user == user
    assert order.items == items
    assert order.address == '123 Main St'
    assert order.payment_method == 'credit_card'
    assert order.status == 'Processing'


def test_order_initialization_multiple_items():
    """
    General Case: Initialize an order with multiple items.
    """
    user = User('janedoe', 'Password456!', 'janedoe@example.com')
    product1 = Product('Laptop', 999.99, 'A high-performance laptop')
    product2 = Product('Smartphone', 599.99, 'A powerful smartphone')
    items = [{'product': product1, 'quantity': 1}, {'product': product2, 'quantity': 2}]
    order = Order(user, items, '456 Elm St', 'debit_card')
    
    assert order.user == user
    assert order.items == items
    assert order.address == '456 Elm St'
    assert order.payment_method == 'debit_card'
    assert order.status == 'Processing'


def test_order_initialization_with_different_payment_methods():
    """
    General Case: Initialize an order with different valid payment methods.
    """
    user = User('mikedoe', 'Password789!', 'mikedoe@example.com')
    product = Product('Tablet', 299.99, 'A versatile tablet')
    items = [{'product': product, 'quantity': 3}]
    
    # Test with 'paypal'
    order_paypal = Order(user, items, '789 Oak St', 'paypal')
    assert order_paypal.payment_method == 'paypal'
    
    # Test with 'credit_card'
    order_credit = Order(user, items, '789 Oak St', 'credit_card')
    assert order_credit.payment_method == 'credit_card'
    
    # Test with 'debit_card'
    order_debit = Order(user, items, '789 Oak St', 'debit_card')
    assert order_debit.payment_method == 'debit_card'

# Edge Test Cases for Order Class __init__ Method


# Edge Case: User is None (invalid)
def test_order_initialization_user_none():
    """
    Edge Case: Initialize an order with a None user (invalid).
    """
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 2}]
    with pytest.raises(ValueError):
        Order(None, items, '123 Main St', 'credit_card')

# Edge Case: Items list is empty (invalid)
def test_order_initialization_empty_items():
    """
    Edge Case: Initialize an order with an empty items list (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError):
        Order(user, [], '123 Main St', 'credit_card')

# Edge Case: Items list contains a None value (invalid)
def test_order_initialization_items_with_none():
    """
    Edge Case: Initialize an order with an items list containing None (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    items = [None]
    with pytest.raises(ValueError):
        Order(user, items, '123 Main St', 'credit_card')

# Edge Case: Items list contains a product with quantity 0 (invalid)
def test_order_initialization_item_with_zero_quantity():
    """
    Edge Case: Initialize an order with an item that has quantity 0 (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 0}]
    with pytest.raises(ValueError):
        Order(user, items, '123 Main St', 'credit_card')

# Edge Case: Address length is exactly 0 characters (invalid)
def test_order_initialization_empty_address():
    """
    Edge Case: Initialize an order with an empty address (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    with pytest.raises(ValueError):
        Order(user, items, '', 'credit_card')

# Edge Case: Address length is exactly 1 or 100 characters
def test_order_initialization_boundary_address_length():
    """
    Edge Case: Initialize an order with address length exactly 1 or 100 characters.
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    
    # Address length 1
    order_min_address = Order(user, items, 'A', 'credit_card')
    assert order_min_address.address == 'A'
    
    # Address length 100
    max_address = 'A' * 100
    order_max_address = Order(user, items, max_address, 'credit_card')
    assert order_max_address.address == max_address

# Edge Case: Address exceeds 100 characters (invalid)
def test_order_initialization_long_address():
    """
    Edge Case: Initialize an order with an address exceeding 100 characters (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    long_address = 'A' * 101
    with pytest.raises(ValueError):
        Order(user, items, long_address, 'credit_card')

# Edge Case: Address with special characters
def test_order_initialization_special_characters_address():
    """
    Edge Case: Initialize an order with an address containing special characters.
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    special_address = '123 Main St. #!@'
    order = Order(user, items, special_address, 'credit_card')
    assert order.address == special_address

# Edge Case: Address with non-printable characters (invalid)
def test_order_initialization_non_printable_address():
    """
    Edge Case: Initialize an order with an address containing non-printable characters (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    non_printable_address = '123 Main St.\x00'
    with pytest.raises(ValueError):
        Order(user, items, non_printable_address, 'credit_card')

# Edge Case: Address with only spaces (invalid)
def test_order_initialization_address_only_spaces():
    """
    Edge Case: Initialize an order with an address containing only spaces (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    with pytest.raises(ValueError):
        Order(user, items, '   ', 'credit_card')

# Edge Case: Payment method is exactly one of the allowed values
def test_order_initialization_valid_payment_method():
    """
    Edge Case: Initialize an order with a valid payment method.
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    
    valid_methods = ['credit_card', 'debit_card', 'paypal']
    for method in valid_methods:
        order = Order(user, items, '123 Main St', method)
        assert order.payment_method == method

# Edge Case: Payment method is an empty string (invalid)
def test_order_initialization_empty_payment_method():
    """
    Edge Case: Initialize an order with an empty payment method (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    with pytest.raises(ValueError):
        Order(user, items, '123 Main St', '')

# Edge Case: Payment method with spaces (invalid)
def test_order_initialization_payment_method_spaces():
    """
    Edge Case: Initialize an order with a payment method containing spaces (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    with pytest.raises(ValueError):
        Order(user, items, '123 Main St', '  credit_card  ')

# Edge Case: Payment method with case variations (invalid)
def test_order_initialization_payment_method_case_variations():
    """
    Edge Case: Initialize an order with a payment method using different cases (invalid).
    """
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    with pytest.raises(ValueError):
        Order(user, items, '123 Main St', 'Credit_Card')

# Edge Test Cases for Order Class update_status Method
# Helper function to create an order for testing
def create_order_with_status(initial_status='Processing'):
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    product = Product('Laptop', 999.99, 'A high-performance laptop')
    items = [{'product': product, 'quantity': 1}]
    order = Order(user, items, '123 Main St', 'credit_card')
    order.status = initial_status
    return order

# Edge Case: New status is an empty string (invalid)
def test_update_status_empty_string():
    """
    Edge Case: Attempt to update the status with an empty string (invalid).
    """
    order = create_order_with_status('Processing')
    with pytest.raises(ValueError):
        order.update_status('')

# Edge Case: New status is a valid value but in different cases (e.g., 'processing', 'SHIPPED')
def test_update_status_case_variations():
    """
    Edge Case: Attempt to update the status with a valid value but different cases (invalid).
    """
    order = create_order_with_status('Processing')
    with pytest.raises(ValueError):
        order.update_status('shipped')  # Valid statuses should be case-sensitive
    with pytest.raises(ValueError):
        order.update_status('DELIVERED')

# Edge Case: Status changes follow a logical progression (e.g., cannot skip from 'Processing' to 'Delivered')
def test_update_status_invalid_progression():
    """
    Edge Case: Attempt to change the status in an invalid progression (e.g., skip from 'Processing' to 'Delivered').
    """
    order = create_order_with_status('Processing')
    with pytest.raises(ValueError):
        order.update_status('Delivered')  # Should raise an error as it should be 'Shipped' first

# Edge Case: Invalid status transitions (e.g., 'Delivered' to 'Processing')
def test_update_status_invalid_transition():
    """
    Edge Case: Attempt to update the status from 'Delivered' to 'Processing' (invalid transition).
    """
    order = create_order_with_status('Delivered')
    with pytest.raises(ValueError):
        order.update_status('Processing')  # Invalid backward transition

# Edge Case: Transition from 'Cancelled' to any other status (invalid)
def test_update_status_from_cancelled():
    """
    Edge Case: Attempt to update the status from 'Cancelled' to any other status (invalid).
    """
    order = create_order_with_status('Cancelled')
    with pytest.raises(ValueError):
        order.update_status('Processing')
    with pytest.raises(ValueError):
        order.update_status('Shipped')

# Edge Case: Status change to the same status (e.g., 'Processing' to 'Processing')
def test_update_status_to_same_status():
    """
    Edge Case: Attempt to update the status to the same status (no change).
    """
    order = create_order_with_status('Processing')
    order.update_status('Processing')  # No exception should be raised
    assert order.status == 'Processing'

###############################
### class EcommerceApp Tests ###
###############################


# General Test Case 1: Initialize the EcommerceApp
def test_initialize_ecommerce_app():
    """
    General Case: Ensure the application initializes correctly with empty user, product, and order lists.
    """
    app = EcommerceApp()
    assert len(app.users) == 0  # No users should be registered at initialization
    assert len(app.products) == 0  # No products should be added at initialization
    assert len(app.orders) == 0  # No orders should be present at initialization
    assert len(app.carts) == 0  # No carts should be initialized for any user

# General Test Case 2: Register a new user
def test_register_new_user():
    """
    General Case: Register a new user and ensure the user is added to the users list.
    """
    app = EcommerceApp()
    result = app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    assert result is True  # User should be successfully registered
    assert len(app.users) == 1  # The number of users should be 1 after registration
    assert 'johndoe' in app.users  # The username should be in the users dictionary
    assert isinstance(app.users['johndoe'], User)  # The registered user should be an instance of the User class

# General Test Case 3: Add a new product
def test_add_new_product():
    """
    General Case: Add a new product and ensure it is added to the products list.
    """
    app = EcommerceApp()
    result = app.add_product('Laptop', 999.99, 'A high-performance laptop')
    assert result is True  # Product should be successfully added
    assert len(app.products) == 1  # The number of products should be 1 after addition
    product = app.products[0]  # Retrieve the added product
    assert isinstance(product, Product)  # The added product should be an instance of the Product class
    assert product.name == 'Laptop'  # Verify product name
    assert product.price == 999.99  # Verify product price
    assert product.description == 'A high-performance laptop'  # Verify product description

# Edge Test Cases for register_user Method
# Edge Case 1: Username and email are already taken
def test_register_user_duplicate_username_email():
    """
    Edge Case: Attempt to register a user with a username and email that are already taken.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Username or email already exists"):
        app.register_user('johndoe', 'DifferentPass1!', 'johndoe@example.com')  # Both username and email are taken

# Edge Case 2: Username length is exactly 3 or 20 characters
def test_register_user_username_length_boundary():
    """
    Edge Case: Register users with usernames that are exactly 3 or 20 characters long.
    """
    app = EcommerceApp()
    assert app.register_user('abc', 'Password123!', 'abc@example.com')  # Username with length 3
    assert app.register_user('a' * 20, 'Password123!', 'longusername@example.com')  # Username with length 20

# Edge Case 3: Username with spaces or special characters
def test_register_user_invalid_username_with_spaces_special_chars():
    """
    Edge Case: Attempt to register a user with a username that contains spaces or special characters.
    """
    app = EcommerceApp()
    with pytest.raises(ValueError, match="Invalid username"):
        app.register_user('john doe', 'Password123!', 'johndoe@example.com')  # Username with spaces
    with pytest.raises(ValueError, match="Invalid username"):
        app.register_user('john@doe', 'Password123!', 'johndoe2@example.com')  # Username with special characters

# Edge Case 4: Password length is exactly 8 or 20 characters
def test_register_user_password_length_boundary():
    """
    Edge Case: Register users with passwords that are exactly 8 or 20 characters long.
    """
    app = EcommerceApp()
    assert app.register_user('janedoe', 'Pass123!', 'janedoe@example.com')  # Password with length 8
    assert app.register_user('jackdoe', 'Password123456789!', 'jackdoe@example.com')  # Password with length 20

# Edge Case 5: Password with special characters, without spaces
def test_register_user_password_with_special_characters():
    """
    Edge Case: Register a user with a password containing special characters but without spaces.
    """
    app = EcommerceApp()
    assert app.register_user('janedoe', 'P@ssw0rd!', 'janedoe@example.com')  # Password with special characters

# Edge Case 6: Valid email formats including subdomains and different TLDs up to 10 characters
def test_register_user_valid_email_formats():
    """
    Edge Case: Register users with valid email formats including subdomains and different TLDs up to 10 characters.
    """
    app = EcommerceApp()
    assert app.register_user('janedoe', 'Password123!', 'user@sub.domain.com')  # Email with subdomain
    assert app.register_user('jackdoe', 'Password123!', 'user@domain.co.uk')  # Email with different TLD

# Edge Case 7: Invalid email formats including missing '@', missing domain, invalid characters, spaces, or without a local part
def test_register_user_invalid_email_formats():
    """
    Edge Case: Attempt to register users with invalid email formats.
    """
    app = EcommerceApp()
    with pytest.raises(ValueError, match="Invalid email"):
        app.register_user('janedoe', 'Password123!', 'userdomain.com')  # Missing '@'
    with pytest.raises(ValueError, match="Invalid email"):
        app.register_user('jackdoe', 'Password123!', 'user@.com')  # Missing domain
    with pytest.raises(ValueError, match="Invalid email"):
        app.register_user('mikedoe', 'Password123!', 'user@domain$.com')  # Invalid characters
    with pytest.raises(ValueError, match="Invalid email"):
        app.register_user('janedoe', 'Password123!', ' ')  # Email with only spaces

# Edge Case 8: Email with mixed case
def test_register_user_mixed_case_email():
    """
    Edge Case: Register a user with an email that has mixed case.
    """
    app = EcommerceApp()
    assert app.register_user('johndoe', 'Password123!', 'JohnDoe@Example.com')  # Email with mixed case

# Edge Case 9: Duplicate usernames and emails (case insensitive)
def test_register_user_duplicate_case_insensitive():
    """
    Edge Case: Attempt to register users with usernames and emails that are duplicates in a case-insensitive manner.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Username or email already exists"):
        app.register_user('JohnDoe', 'Password123!', 'johnDoe@example.com')  # Case-insensitive duplicate
# Edge Test Cases for add_product Method
# Edge Case 1: Name length is exactly 1 or 50 characters
def test_add_product_name_length_boundary():
    """
    Edge Case: Add products with names that are exactly 1 or 50 characters long.
    """
    app = EcommerceApp()
    assert app.add_product('A', 100.00, 'A short description')  # Name with length 1
    assert app.add_product('A' * 50, 100.00, 'A short description')  # Name with length 50

# Edge Case 2: Name with special characters
def test_add_product_name_with_special_characters():
    """
    Edge Case: Add a product with a name that contains special characters.
    """
    app = EcommerceApp()
    assert app.add_product('Product@123', 100.00, 'Special character in name')  # Name with special characters

# Edge Case 3: Price is at the minimum (0.01) or maximum (10000.00) value
def test_add_product_price_boundary():
    """
    Edge Case: Add products with prices at the minimum or maximum allowed values.
    """
    app = EcommerceApp()
    assert app.add_product('CheapProduct', 0.01, 'Minimum price product')  # Minimum price
    assert app.add_product('ExpensiveProduct', 10000.00, 'Maximum price product')  # Maximum price

# Edge Case 4: Price with very small decimals
def test_add_product_price_with_small_decimals():
    """
    Edge Case: Add a product with a price that has very small decimals.
    """
    app = EcommerceApp()
    assert app.add_product('TinyDecimalProduct', 0.001, 'Price with very small decimals')

# Edge Case 5: Description length is exactly 0 or 200 characters
def test_add_product_description_length_boundary():
    """
    Edge Case: Add products with descriptions that are exactly 0 or 200 characters long.
    """
    app = EcommerceApp()
    assert app.add_product('ProductNoDescription', 100.00, '')  # Description with length 0
    assert app.add_product('LongDescriptionProduct', 100.00, 'A' * 200)  # Description with length 200

# Edge Case 6: Description with special characters and emojis
def test_add_product_description_with_special_chars_emojis():
    """
    Edge Case: Add a product with a description containing special characters and emojis.
    """
    app = EcommerceApp()
    assert app.add_product('SpecialProduct', 100.00, 'Description with special characters! 😊')

# Edge Case 7: Very long description
def test_add_product_very_long_description():
    """
    Edge Case: Attempt to add a product with a description that is too long.
    """
    app = EcommerceApp()
    with pytest.raises(ValueError, match="Description length exceeds 200 characters"):
        app.add_product('TooLongDescriptionProduct', 100.00, 'A' * 201)  # Description with length 201

# Edge Case 8: Empty name or name with just spaces
def test_add_product_empty_name_or_spaces():
    """
    Edge Case: Attempt to add a product with an empty name or a name consisting of only spaces.
    """
    app = EcommerceApp()
    with pytest.raises(ValueError, match="Invalid product name"):
        app.add_product('', 100.00, 'Valid description')  # Empty name
    with pytest.raises(ValueError, match="Invalid product name"):
        app.add_product('   ', 100.00, 'Valid description')  # Name with only spaces

# Edge Case 9: Zero or negative prices
def test_add_product_invalid_prices():
    """
    Edge Case: Attempt to add products with zero or negative prices.
    """
    app = EcommerceApp()
    with pytest.raises(ValueError, match="Invalid price"):
        app.add_product('ZeroPriceProduct', 0.00, 'Zero price is invalid')  # Price is zero
    with pytest.raises(ValueError, match="Invalid price"):
        app.add_product('NegativePriceProduct', -100.00, 'Negative price is invalid')  # Negative price

# Edge Test Cases for add_to_cart Method
# Edge Case 1: Quantity is exactly 1 or 100
def test_add_to_cart_quantity_boundary():
    """
    Edge Case: Add a product to the cart with a quantity of exactly 1 or 100.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    assert app.add_to_cart('johndoe', 0, 1)  # Quantity is 1
    assert app.add_to_cart('johndoe', 0, 100)  # Quantity is 100

# Edge Case 2: Adding the same product multiple times should combine quantities or update existing quantity
def test_add_to_cart_combining_quantities():
    """
    Edge Case: Add the same product multiple times, expecting quantities to combine.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    app.add_to_cart('johndoe', 0, 1)
    app.add_to_cart('johndoe', 0, 2)
    cart = app.carts['johndoe'].view_cart()
    assert cart[0]['quantity'] == 3  # Combined quantity

# Edge Case 3: Adding a product with quantity less than 1 or more than 100 (invalid)
def test_add_to_cart_invalid_quantity():
    """
    Edge Case: Attempt to add a product with a quantity less than 1 or more than 100.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    with pytest.raises(ValueError, match="Invalid quantity"):
        app.add_to_cart('johndoe', 0, 0)  # Quantity less than 1
    with pytest.raises(ValueError, match="Invalid quantity"):
        app.add_to_cart('johndoe', 0, 101)  # Quantity more than 100

# Edge Case 4: Invalid product ID
def test_add_to_cart_invalid_product_id():
    """
    Edge Case: Attempt to add a product to the cart with an invalid product ID.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Invalid product ID"):
        app.add_to_cart('johndoe', -1, 1)  # Negative product ID

# Edge Case 5: Adding to cart without being logged in
def test_add_to_cart_without_login():
    """
    Edge Case: Attempt to add a product to the cart without being logged in.
    """
    app = EcommerceApp()
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    with pytest.raises(ValueError, match="User not registered"):
        app.add_to_cart('unregistered_user', 0, 1)  # Unregistered user

# Edge Test Cases for checkout Method
# Edge Case 1: Address length is exactly 1 or 100 characters
def test_checkout_address_length_boundary():
    """
    Edge Case: Checkout with addresses that are exactly 1 or 100 characters long.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    app.add_to_cart('johndoe', 0, 2)
    assert app.checkout('johndoe', 'A', 'credit_card') != -1  # Address with length 1
    assert app.checkout('johndoe', 'A' * 100, 'credit_card') != -1  # Address with length 100

# Edge Case 2: Address with special characters
def test_checkout_address_with_special_characters():
    """
    Edge Case: Checkout with an address that contains special characters.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    app.add_to_cart('johndoe', 0, 2)
    assert app.checkout('johndoe', '@123 Main St!$', 'credit_card') != -1  # Address with special characters

# Edge Case 3: Payment method is exactly one of the allowed values
def test_checkout_valid_payment_methods():
    """
    Edge Case: Checkout with valid payment methods.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    app.add_to_cart('johndoe', 0, 2)
    assert app.checkout('johndoe', '123 Main St', 'credit_card') != -1  # Valid payment method

# Edge Case 4: Empty cart checkout
def test_checkout_empty_cart():
    """
    Edge Case: Attempt to checkout with an empty cart.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Cart is empty"):
        app.checkout('johndoe', '123 Main St', 'credit_card')  # Empty cart

# Edge Case 5: Payment method with spaces (invalid)
def test_checkout_invalid_payment_method_with_spaces():
    """
    Edge Case: Attempt to checkout with an invalid payment method containing spaces.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    app.add_to_cart('johndoe', 0, 2)
    with pytest.raises(ValueError, match="Invalid payment method"):
        app.checkout('johndoe', '123 Main St', 'credit card')  # Payment method with spaces

# Edge Test Cases for track_order Method
# Edge Case: Invalid order IDs, including negative values and excessively large values
def test_track_order_invalid_order_ids():
    """
    Edge Case: Attempt to track orders with invalid order IDs such as negative values or excessively large values.
    """
    app = EcommerceApp()
    app.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    app.add_product('Laptop', 999.99, 'A high-performance laptop')
    app.add_to_cart('johndoe', 0, 2)
    order_id = app.checkout('johndoe', '123 Main St', 'credit_card')
    
    with pytest.raises(ValueError, match="Invalid order ID"):
        app.track_order(-1)  # Negative order ID
    
    with pytest.raises(ValueError, match="Invalid order ID"):
        app.track_order(999999)  # Excessively large order ID


pytest.main()
