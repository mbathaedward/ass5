import csv
import os

# File path for the CSV file
FILE_PATH = 'products.csv'

# Function to initialize the CSV file
def initialize_csv(file_path):
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price', 'Quantity'])

# Function to add  product
def add_product(file_path, name, price, quantity):
    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, price, quantity])
        print(f"Product '{name}' added successfully.")
    except Exception as e:
        print(f"Error adding product: {e}")

# Function to view all products
def view_products(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            products = list(reader)
            if not products:
                print("No products available.")
            else:
                for product in products:
                    print(f"Name: {product[0]}, Price: {product[1]}, Quantity: {product[2]}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error viewing products: {e}")

# Function to update a product
def update_product(file_path, name, new_price=None, new_quantity=None):
    try:
        updated = False
        products = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for product in reader:
                if product[0] == name:
                    if new_price is not None:
                        product[1] = new_price
                    if new_quantity is not None:
                        product[2] = new_quantity
                    updated = True
                products.append(product)
        
        if updated:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print(f"Product '{name}' updated successfully.")
        else:
            print(f"Product '{name}' not found.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error updating product: {e}")

# Function to delete a product
def delete_product(file_path, name):
    try:
        deleted = False
        products = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for product in reader:
                if product[0] != name:
                    products.append(product)
                else:
                    deleted = True
        
        if deleted:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print(f"Product '{name}' deleted successfully.")
        else:
            print(f"Product '{name}' not found.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting product: {e}")

# Main program loop
def main():
    initialize_csv(FILE_PATH)

    while True:
        print("\nProduct Management System")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = input("Enter product quantity: ")
            add_product(FILE_PATH, name, price, quantity)
        elif choice == '2':
            view_products(FILE_PATH)
        elif choice == '3':
            name = input("Enter the product name to update: ")
            new_price = input("Enter new price (leave blank to keep current): ")
            new_quantity = input("Enter new quantity (leave blank to keep current): ")
            new_price = new_price if new_price else None
            new_quantity = new_quantity if new_quantity else None
            update_product(FILE_PATH, name, new_price, new_quantity)
        elif choice == '4':
            name = input("Enter the product name to delete: ")
            delete_product(FILE_PATH, name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()