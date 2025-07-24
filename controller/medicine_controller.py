
class MedicineController:
    def __init__(self, medicine_dao, medicine_view, user_id):
        self.dao = medicine_dao
        self.view = medicine_view
        self.user_id = user_id

    def add_medicine(self):
        name, company, quantity, expiry = self.view.get_medicine_details()
        self.dao.insert_medicine(name, company, quantity, expiry, self.user_id)
        self.view.show_message("Medicine added successfully!")

    def view_medicines(self):
        medicines = self.dao.fetch_medicines_by_user(self.user_id)
        self.view.show_medicines(medicines)

    def search_medicine(self):
        name = self.view.get_search_name()
        results = self.dao.search_medicine(name, self.user_id)
        self.view.show_medicines(results)

    def update_medicine(self):
        id = self.view.get_id("update")
        name, company, quantity, expiry = self.view.get_medicine_details()
        self.dao.update_medicine(id, name, company, quantity, expiry, self.user_id)
        self.view.show_message("Medicine updated successfully!")

    def delete_medicine(self):
        id = self.view.get_id("delete")
        self.dao.delete_medicine(id, self.user_id)
        self.view.show_message("Medicine deleted successfully!")
