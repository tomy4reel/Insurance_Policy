# policyholder.py
class Policyholder:
    def __init__(self, policyholder_id, name, is_active=True):
        self.policyholder_id = policyholder_id
        self.name = name
        self.is_active = is_active
        self.products = []

    def register(self, product):
        self.products.append(product)
        print(f"{self.name} has registered for product {product.name}.")

    def suspend(self):
        self.is_active = False
        print(f"{self.name}'s account has been suspended.")

    def reactivate(self):
        self.is_active = True
        print(f"{self.name}'s account has been reactivated.")

    def display_details(self):
        status = "Active" if self.is_active else "Suspended"
        product_names = [product.name for product in self.products]
        print(f"Policyholder ID: {self.policyholder_id}\n"
              f"Name: {self.name}\n"
              f"Status: {status}\n"
              f"Products: {', '.join(product_names)}")
