# Policy Management System

## Overview
This Policy Management System allows an insurance company to manage policyholders, products, and payments. The system provides functionalities to add, suspend, and reactivate policyholders; manage policy products; and process payments. The codebase is modular, with separate classes for policyholders, products, and payments, ensuring clean and maintainable code.

## Project Structure
The project consists of the following main components:

1. **Policyholder Management (`policyholder.py`)**: Manages the details and operations related to policyholders.
2. **Product Management (`product.py`)**: Manages the details and operations related to policy products.
3. **Payment Management (`payment.py`)**: Manages the payment processing, reminders, and penalties.
4. **Main Demonstration (`main.py`)**: Demonstrates the usage of the classes and methods to manage policyholders, products, and payments.

## Setup and Installation
1. **Clone the Repository**: Start by cloning the repository to your local machine.

2. **Navigate to the Project Directory**: Change to the project directory using the command line.

3. **Install Dependencies**: If there are any dependencies, they will be listed in a `requirements.txt` file. Install them using the following command:
   ```
   pip install -r requirements.txt
   ```

4. **Running the Application**: To run the application and see the demonstration, execute the `main.py` script using Python. This script showcases the functionalities provided by the classes.

## Usage
### Policyholder Management
- **Register a Policyholder**: Create a new instance of the `Policyholder` class and call the `register` method with the desired product.
- **Suspend a Policyholder**: Use the `suspend` method to mark a policyholder's account as suspended.
- **Reactivate a Policyholder**: Use the `reactivate` method to mark a policyholder's account as active.
- **Display Policyholder Details**: Use the `display_details` method to print the details of a policyholder.

### Product Management
- **Create a Product**: Create a new instance of the `Product` class with the required details.
- **Update a Product**: Use the `update` method to modify the product's name or description.
- **Suspend a Product**: Use the `suspend` method to mark the product as inactive.

### Payment Management
- **Process a Payment**: Create a new instance of the `Payment` class and call the `process_payment` method to mark the payment as completed.
- **Send Payment Reminders**: Use the `send_reminder` method to notify policyholders of due payments.
- **Apply Penalties**: Use the `apply_penalty` method to add a penalty amount to a payment.

## Example Demonstration
In the `main.py` file, there are examples demonstrating how to create policyholders, products, and payments. The examples show how to register policyholders for products, process payments, and manage accounts.

## Notes
- The system currently uses in-memory data storage. For production use, consider integrating a database for persistent data storage.
- Proper error handling should be implemented for a more robust system, especially for real-world applications.
