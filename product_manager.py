from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} is added to the list.")

    def info_products(self):
        if not self.products:
            print("List is empty.")
        else:
            print("Products on the list:")
            for product in self.products:
                print(product.info_product())

    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"The total value in the basket: {total:.2f} $")

    def removing_product(self):
        product_name = input("Enter name of product:").strip().lower()
        for product in self.products:
            if product.name.strip().lower() == product_name:
                self.products.remove(product)
                print(f"Product {product_name} is removed from the list")
                break
            else:
                print("Product is not on the list")
