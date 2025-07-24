
from model.db_connection import get_connection

class MedicineDAO:
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS medicines (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100),
                company VARCHAR(100),
                quantity INT,
                expiry DATE,
                user_id INT
            )
        ''')
        self.conn.commit()

    def insert_medicine(self, name, company, quantity, expiry, user_id):
        self.cur.execute(
            "INSERT INTO medicines (name, company, quantity, expiry, user_id) VALUES (?, ?, ?, ?, ?)",
            (name, company, quantity, expiry, user_id)
        )
        self.conn.commit()

    def fetch_medicines_by_user(self, user_id):
        self.cur.execute("SELECT * FROM medicines WHERE user_id=?", (user_id,))
        return self.cur.fetchall()

    def search_medicine(self, name, user_id):
        self.cur.execute("SELECT * FROM medicines WHERE name LIKE ? AND user_id=?", ('%' + name + '%', user_id))
        return self.cur.fetchall()

    def update_medicine(self, id, name, company, quantity, expiry, user_id):
        self.cur.execute(
            "UPDATE medicines SET name=?, company=?, quantity=?, expiry=? WHERE id=? AND user_id=?",
            (name, company, quantity, expiry, id, user_id)
        )
        self.conn.commit()

    def delete_medicine(self, id, user_id):
        self.cur.execute("DELETE FROM medicines WHERE id=? AND user_id=?", (id, user_id))
        self.conn.commit()
