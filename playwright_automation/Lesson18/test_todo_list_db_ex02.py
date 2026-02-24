
import sqlite3
import playwright
import pytest

from playwright_automation.Lesson18.todo_list_pom import TodoListPage


class TestDBExample02:

    @pytest.fixture(scope="class",autouse=True)
    def setup(self, playwright: playwright):
        global browser, context, page, my_db,todo_list
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playground.atidcollege.co.il/todo-list/index.html")
        db_path = r"playwright_automation\Lesson18\tasks.db"
        my_db = sqlite3.connect(db_path)
        todo_list = TodoListPage(page)
        yield
        my_db.close()

    def test01_verify_add_task(self):
        query = "SELECT * FROM tasks"
        my_cursor = my_db.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        print(my_result)
        for row in my_result:
            todo_list.add_task(row[1])
        assert todo_list.get_total_task() == 3

            