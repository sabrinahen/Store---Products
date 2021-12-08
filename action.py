import product
import store 

sabrina = Store("Sabrina's Store")
apple = Product("apple", 5, "Fruit")
chicken = Product("chicken", 10, "Meat")
steak = Product("steak", 40, "Meat")
banana = Product("banana", 3, "Fruit")

sabrina.add_products(apple).add_products(chicken).add_products(steak).add_products(banana)

sabrina.set_clearance("Fruit", .2)

apple.print_info()