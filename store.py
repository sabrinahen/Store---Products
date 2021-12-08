# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
    
#     def update_price(self, percent_change, is_increased):
#         if is_increased is True:
#             self.price += (self.price * percent_change)
#             print(self.price)
#         else:
#             self.price -= (self.price * percent_change)
#             print(self.price)

#     def print_info(self):
#         print(f"Name: {self.name}, Price: {self.price}, Category: {self.category}")
#         return self

import product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_products(self, new_product):
        self.products.append(new_product)
        theInventory = []
        for p in self.products:
            theInventory.append(p.name)
        print(theInventory)
        return self

    def sell_product(self, id):
        print("Item has been sold!")
        self.products[id].print_info()
        self.products.remove(id)
    
    def inflation(self, percent_increase):
        for product in self.products: 
            product.update_price(percent_increase, True)
        print(self.price)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.price -= (product.price * percent_discount)
        return self

# sabrina = Store("Sabrina's Store")
# apple = Product("apple", 5, "Fruit")
# chicken = Product("chicken", 10, "Meat")
# steak = Product("steak", 40, "Meat")
# banana = Product("banana", 3, "Fruit")

# sabrina.add_products(apple).add_products(chicken).add_products(steak).add_products(banana)

# sabrina.set_clearance("Fruit", .2)

# apple.print_info()