import sqlite3

class DBActions:
    def __init__(self,db_path):
        self.db = sqlite3.connect(db_path)

    def close_db(self):
        self.db.close()

    def get_admin_user(self)->dict:
        query = "SELECT * FROM users"
        my_cursor = self.db.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        admin_user ={"user_name":my_result[0][0],"password":my_result[0][1]}
        return admin_user