import sys
import pytest
from loguru import logger
from homeworks.hw21.source.library.book import Book

logger.remove()
logger.add(sys.stderr, level="INFO")


class TestBook:

    @pytest.fixture
    def book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        logger.debug("Book created")
        return book

    def test_reserve_free(self, book):
        result = book.reserve("James Bond")
        logger.info("Reserve the book")
        assert result is True

    def test_reserve_already_reserved_by_same_reader(self, book):
        book.reserve("James Bond")
        result = book.reserve("James Bond")
        logger.info("The book already reserved same reader")
        assert result is False

    def test_reserve_already_reserved_by_different_reader(self, book):
        book.reserve("James Bond")
        result = book.reserve("Guy Ritchie")
        logger.info("The book already reserved different reader")
        assert result is False

    def test_reserve_issued_book(self, book):
        book.get_book("James Bond")
        result = book.reserve("Guy Ritchie")
        logger.info("The book successfully reserved")
        assert result is True

    def test_cancel_reserve_same_reader(self, book):
        book.reserve("James Bond")
        result = book.cancel_reserve("James Bond")
        logger.info("The book successfully cancelled")
        assert result is True

    def test_cancel_reserve_different_reader(self, book):
        book.reserve("James Bond")
        result = book.cancel_reserve("Guy Ritchie")
        logger.info("Reservation cannot be cancelled")
        assert result is False

    def test_cancel_reserve_no_reservation(self, book):
        result = book.cancel_reserve("James Bond")
        logger.info("Reservation cannot be cancelled")
        assert result is False

    def test_get_book_free(self, book):
        result = book.get_book("James Bond")
        logger.info("Free book has been issued")
        assert result is True

    def test_get_book_reserved_by_same_reader(self, book):
        book.reserve("James Bond")
        result = book.get_book("James Bond")
        logger.info("Reserve book has been issued")
        assert result is True

    def test_get_book_reserved_by_different_reader(self, book):
        book.reserve("James Bond")
        result = book.get_book("Guy Ritchie")
        logger.info("The book already reserved different reader")
        assert result is False

    def test_get_book_issued_book(self, book):
        book.get_book("James Bond")
        result = book.get_book("Guy Ritchie")
        logger.info("The book was issued")
        assert result is False

    def test_return_book_same_reader(self, book):
        book.get_book("James Bond")
        result = book.return_book("James Bond")
        logger.info("The book was returned")
        assert result is True

    def test_return_book_not_issued(self, book):
        result = book.return_book("James Bond")
        logger.info("The book was not issued")
        assert result is False
