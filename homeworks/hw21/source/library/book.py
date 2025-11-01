class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved_by = None
        self.issued_to = None

    def reserve(self, reader_name):
        if self.issued_to and self.issued_to == reader_name:
            return False
        if self.reserved_by and self.reserved_by != reader_name:
            return False
        if self.issued_to and self.issued_to != reader_name:
            if self.reserved_by is None:
                self.reserved_by = reader_name
                return True
        if self.reserved_by == reader_name:
            return False
        if self.issued_to is None and self.reserved_by is None:
            self.reserved_by = reader_name
            return True
        return False

    def cancel_reserve(self, reader_name):
        if self.reserved_by is None:
            return False
        if self.reserved_by != reader_name:
            return False
        self.reserved_by = None
        return True

    def get_book(self, reader_name):
        if self.issued_to is not None:
            return False
        if self.reserved_by and self.reserved_by != reader_name:
            return False
        self.issued_to = reader_name
        if self.reserved_by == reader_name:
            self.reserved_by = None
        return True

    def return_book(self, reader_name):
        if self.issued_to is None:
            return False
        if self.issued_to != reader_name:
            return False
        self.issued_to = None
        return True
