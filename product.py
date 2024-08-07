# product.py
class Product:
    def __init__(self, product_id, name, description, is_active=True):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.is_active = is_active

    def update(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        print(f"Product {self.product_id} has been updated.")

    def suspend(self):
        self.is_active = False
        print(f"Product {self.product_id} has been suspended.")
