from .book import Book


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book: Book):
        return book.reserve(self.name)

    def cancel_reserve(self, book: Book):
        return book.cancel_reserve(self.name)

    def get_book(self, book: Book):
        return book.get_book(self.name)

    def return_book(self, book: Book):
        return book.return_book(self.name)
