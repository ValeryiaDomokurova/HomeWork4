import unittest
from .book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        print("Book created")

    def test_reserve_free(self):
        result = self.book.reserve("James Bond")
        self.assertTrue(result)
        self.assertEqual(self.book.reserved_by, "James Bond")
        print("The book successfully reserved")

    def test_reserve_already_reserved_by_same_reader(self):
        self.book.reserve("James Bond")
        result = self.book.reserve("James Bond")
        self.assertFalse(result)
        self.assertEqual(self.book.reserved_by, "James Bond")
        print("The book already reserved same reader")

    def test_reserve_already_reserved_by_different_reader(self):
        self.book.reserve("James Bond")
        result = self.book.reserve("Guy Ritchie")
        self.assertFalse(result)
        self.assertEqual(self.book.reserved_by, "James Bond")
        print("The book already reserved different reader")

    def test_reserve_issued_book(self):
        self.book.get_book("James Bond")
        result = self.book.reserve("Guy Ritchie")
        self.assertTrue(result)
        self.assertEqual(self.book.reserved_by, "Guy Ritchie")
        self.assertEqual(self.book.issued_to, "James Bond")
        print("The book successfully reserved")

    def test_cancel_reserve_same_reader(self):
        self.book.reserve("James Bond")
        result = self.book.cancel_reserve("James Bond")
        self.assertTrue(result)
        self.assertIsNone(self.book.reserved_by)
        print("The book successfully cancelled")

    def test_cancel_reserve_different_reader(self):
        self.book.reserve("James Bond")
        result = self.book.cancel_reserve("Guy Ritchie")
        self.assertFalse(result)
        self.assertEqual(self.book.reserved_by, "James Bond")
        print("Reservation cannot be cancelled")

    def test_cancel_reserve_no_reservation(self):
        result = self.book.cancel_reserve("James Bond")
        self.assertFalse(result)
        self.assertIsNone(self.book.reserved_by)
        print("Reservation cannot be cancelled")

    def test_get_book_free(self):
        result = self.book.get_book("James Bond")
        self.assertTrue(result)
        self.assertEqual(self.book.issued_to, "James Bond")
        print("Free book has been issued")

    def test_get_book_reserved_by_same_reader(self):
        self.book.reserve("James Bond")
        result = self.book.get_book("James Bond")
        self.assertTrue(result)
        self.assertEqual(self.book.issued_to, "James Bond")
        self.assertIsNone(self.book.reserved_by)
        print("The book was issued")

    def test_get_book_reserved_by_different_reader(self):
        self.book.reserve("James Bond")
        result = self.book.get_book("Guy Ritchie")
        self.assertFalse(result)
        self.assertEqual(self.book.reserved_by, "James Bond")
        print("The book already reserved different reader")

    def test_get_book_issued_book(self):
        self.book.get_book("James Bond")
        result = self.book.get_book("Guy Ritchie")
        self.assertFalse(result)
        self.assertEqual(self.book.issued_to, "James Bond")
        print("The book was issued")

    def test_return_book_same_reader(self):
        self.book.get_book("James Bond")
        result = self.book.return_book("James Bond")
        self.assertTrue(result)
        self.assertIsNone(self.book.issued_to)
        print("The book was returned")

    def test_return_book_not_issued(self):
        result = self.book.return_book("James Bond")
        self.assertFalse(result)
        self.assertIsNone(self.book.issued_to)
        print("The book was not issued")


if __name__ == '__main__':
    unittest.main()
