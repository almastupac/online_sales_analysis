from product import Product
from product_manager import ProductManager

#  Creating instance
manager1 = ProductManager()
product1 = Product('Hat', 19.50, 2)
product2 = Product('Shoes', 79.99, 1)
product3 = Product('Pullover', 75.00, 1)


# Adding products
manager1.add_product(product1)
manager1.add_product(product2)
manager1.add_product(product3)


