
class UserController:
    def __init__(self, user_dao, user_view):
        self.user_dao = user_dao
        self.user_view = user_view

    def authenticate(self):
        while True:
            choice = self.user_view.show_login_menu()
            if choice == '1':
                username, password = self.user_view.get_login_details()
                user = self.user_dao.login(username, password)
                if user:
                    self.user_view.show_message("Login successful!")
                    return user
                else:
                    self.user_view.show_message("Invalid credentials.")
            elif choice == '2':
                username, password = self.user_view.get_login_details()
                if self.user_dao.register(username, password):
                    self.user_view.show_message("Registration successful!")
                else:
                    self.user_view.show_message("Username already exists.")
            elif choice == '3':
                exit()
            else:
                self.user_view.show_message("Invalid choice.")
