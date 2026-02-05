# Parent class
class Product:
    def _init_(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ₹{self.price}")

# Child class inheriting from Product
class ElectronicProduct(Product):
    def _init_(self, product_name, price, brand, warranty):
        super()._init_(product_name, price)  # Calling Product constructor
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        self.display_product()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty}")

# Grandchild class inheriting from ElectronicProduct
class MobilePhone(ElectronicProduct):
    def _init_(self, product_name, price, brand, warranty, ram, storage):
        super()._init_(product_name, price, brand, warranty)  # Calling ElectronicProduct constructor
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        self.display_electronic_product()
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

# Create an object of MobilePhone
mobile_phone = MobilePhone("Samsung Galaxy S22", 79999, "Samsung", "2 years", 8, 128)

# Display mobile phone details
mobile_phone.display_mobile_details()
