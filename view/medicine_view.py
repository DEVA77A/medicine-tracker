
from datetime import datetime

class MedicineView:
    def show_menu(self):
        print("\n--- Medicine Tracker Menu ---")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Search Medicine")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
        return input("Choose an option: ")

    def get_medicine_details(self):
        name = input("Enter medicine name: ")
        company = input("Enter company name: ")
        quantity = int(input("Enter quantity: "))
        expiry = input("Enter expiry date (YYYY-MM-DD): ")
        return name, company, quantity, expiry

    def get_search_name(self):
        return input("Enter medicine name to search: ")

    def get_id(self, action):
        return int(input(f"Enter medicine ID to {action}: "))

    def show_medicines(self, medicines):
        if not medicines:
            print("No medicines found!")
            return
        print("\nID | Name | Company | Quantity | Expiry | Status")
        print("-" * 60)
        today = datetime.today().date()
        for med in medicines:
            expiry = med[4]
            status = "Expired" if expiry < today else "Valid"
            print(f"{med[0]} | {med[1]} | {med[2]} | {med[3]} | {expiry} | {status}")

    def show_message(self, msg):
        print(msg)
