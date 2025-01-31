class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)
        print(f"Product {product.name} added to cart.")

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart_items)
        print(f"Total cart value: {total:.2f} $")

    def info_cart(self):
        if not self.cart_items:
            print("Cart is empty")
        else:
            print("Products in cart:")
            for product in self.cart_items:
                print(f"{product.name} - {product.price} x {product.quantity}")
