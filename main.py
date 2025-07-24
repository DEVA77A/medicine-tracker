
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.user_dao import UserDAO
from model.medicine_dao import MedicineDAO
from controller.user_controller import UserController
from controller.medicine_controller import MedicineController
from view.user_view import UserView
from view.medicine_view import MedicineView

def main():
    user_controller = UserController(UserDAO(), UserView())
    user = user_controller.authenticate()
    user_id = user[0]

    med_controller = MedicineController(MedicineDAO(), MedicineView(), user_id)

    while True:
        choice = med_controller.view.show_menu()
        if choice == '1':
            med_controller.add_medicine()
        elif choice == '2':
            med_controller.view_medicines()
        elif choice == '3':
            med_controller.search_medicine()
        elif choice == '4':
            med_controller.update_medicine()
        elif choice == '5':
            med_controller.delete_medicine()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
