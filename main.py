from product import Product
from product_manager import ProductManager
from cart import Cart


#  Creating instance
manager1 = ProductManager()
product1 = Product('Hat', 19.50, 2)
product2 = Product('Shoes', 79.99, 1)
product3 = Product('Pullover', 75.00, 1)


# Adding products
manager1.add_product(product1)
manager1.add_product(product2)
manager1.add_product(product3)


#  Display products list
print(manager1.info_products())


#  Display total value
print(manager1.total_value())


#  Creating instance class Cart
cart1 = Cart()

#  Adding products
cart1.add_product(product1)
cart1.add_product(product2)
cart1.add_product(product3)

#  Calculat total and display list of products
print(cart1.calculate_total())
print(cart1.info_cart())
