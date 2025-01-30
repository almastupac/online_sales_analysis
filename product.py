class Product:
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def info_product(self):
        return (f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity = amount
        print(f"Quantity of product {self.name} is updated to {self.quantity}")
