class Book :
    def __init__(self, total_pages):
        self.total_pages = total_pages
        self.current_page = 0
    def read_page(self,pages_read):
        self.current_page += pages_read
        if self.current_page >= self.total_pages:
            self.current_page = self.total_pages
            print("Book Finished!")
        pages_left = (self.total_pages - self.current_page)
        print(f"You have {pages_left} pages left to read")

