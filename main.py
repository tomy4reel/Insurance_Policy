# main.py
from policyholder import Policyholder
from product import Product
from payment import Payment

# Creating policyholders
policyholder1 = Policyholder(policyholder_id=1, name="John Doe")
policyholder2 = Policyholder(policyholder_id=2, name="Jane Smith")

# Creating products
product1 = Product(product_id=101, name="Health Insurance", description="Comprehensive health coverage.")
product2 = Product(product_id=102, name="Car Insurance", description="Full coverage car insurance.")

# Registering policyholders for products
policyholder1.register(product1)
policyholder2.register(product2)

# Suspending and reactivating policyholders
policyholder1.suspend()
policyholder1.reactivate()

# Creating payments
payment1 = Payment(payment_id=1001, amount=500, policyholder=policyholder1)
payment2 = Payment(payment_id=1002, amount=300, policyholder=policyholder2)

# Processing payments
payment1.process_payment()
payment2.process_payment()

# Sending payment reminders and applying penalties
payment2.send_reminder()
payment2.apply_penalty(50)

# Displaying policyholder details
policyholder1.display_details()
policyholder2.display_details()
