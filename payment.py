# payment.py
class Payment:
    def __init__(self, payment_id, amount, policyholder, status="Pending"):
        self.payment_id = payment_id
        self.amount = amount
        self.policyholder = policyholder
        self.status = status

    def process_payment(self):
        self.status = "Completed"
        print(f"Payment {self.payment_id} for {self.policyholder.name} has been processed.")

    def send_reminder(self):
        print(f"Reminder: Payment of {self.amount} is due for {self.policyholder.name}.")

    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount
        print(f"Penalty of {penalty_amount} applied to {self.policyholder.name}'s payment.")
