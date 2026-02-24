import sqlite3
import pytest


class TestDBExample:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self):
        global my_db
        db_path = r"playwright_automation\Lesson18\products.db"
        my_db = sqlite3.connect(db_path)
        yield
        my_db.close()

    def test01_verify_db(self):
        query = "SELECT * FROM products"
        my_cursor = my_db.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        print(my_result)

        total_products = len(my_result)
        print(f"\nTotal number of products: {total_products}") 
        
        print("\nItems:")
        sum = 0
        for item in my_result:
            print(item)
            sum+=item[2]
        print(f"The sum is:{sum}")
  
