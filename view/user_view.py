
class UserView:
    def show_login_menu(self):
        print("\n==============================")
        print(" Welcome to Medicine Tracker")
        print("==============================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        return input("Choose option: ")

    def get_login_details(self):
        username = input("Username: ")
        password = input("Password: ")
        return username, password

    def show_message(self, message):
        print(message)
