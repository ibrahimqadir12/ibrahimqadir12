class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)

# Sample Products
product1 = Product("Laptop", 800)
product2 = Product("Phone", 500)

# Sample Customer
customer = Customer("ibrahim")

# Sample Order
order = Order(customer)
order.add_product(product1)
order.add_product(product2)

# Display Order Details
print(f"Order for {order.customer.name}:")
for product in order.products:
    print(f"- {product.name} (pkr-{product.price:.2f})")
print(f"Total: pkr-{order.calculate_total():.2f}")
