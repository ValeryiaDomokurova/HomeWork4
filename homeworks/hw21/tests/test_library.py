# pylint: disable=too-many-public-methods
import pytest
import random
import time
from loguru import logger
from homeworks.hw21.source.library.book import Book


class BookStub:
    def __init__(self):
        self.book_name = "The Book"
        self.author = "The Author"
        self.num_pages = 10
        self.isbn = "123"

class BookFake:
    def __init__(self):
        self.reserved_by = None
        self.issued_to = None


    def reserve(self, reader):
        if self.reserved_by is None:
            self.reserved_by = reader
            return True
        return False

    def cancel_reserve(self, reader):
        if self.reserved_by == reader:
            self.reserved_by = None
            return True
        return False

    def get_book(self, reader):
        if self.issued_to is not None:
            return False
        if self.reserved_by is None or self.reserved_by == reader:
            self.issued_to = reader
            self.reserved_by = None
            return True
        return False

    def return_book(self, reader):
        if self.issued_to == reader:
            self.issued_to = None
            return True
        return False


class TestBook:
    @pytest.fixture
    def book_stub(self):
        return BookStub()

    @pytest.fixture
    def book_fake(self):
        return BookFake()

    @pytest.fixture
    def book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        logger.debug("Book created")
        return book

    def test_reserve_free_fake(self, book_fake):
        result = book_fake.reserve("James Bond")
        logger.info("Fake: Reserve the book")
        assert result is True
        assert book_fake.reserved_by == "James Bond"

    def test_reserve_already_reserved_by_same_reader_fake(self, book_fake):
        book_fake.reserve("James Bond")
        result = book_fake.reserve("James Bond")
        logger.info("Fake: The book already reserved same reader")
        assert result is False
        assert book_fake.reserved_by == "James Bond"

    def test_reserve_already_reserved_by_different_reader_fake(self, book_fake):
        book_fake.reserve("James Bond")
        result = book_fake.reserve("Guy Ritchie")
        logger.info("Fake: The book already reserved different reader")
        assert result is False
        assert book_fake.reserved_by == "James Bond"

    def test_reserve_issued_book_fake(self, book_fake):
        book_fake.get_book("James Bond")
        result = book_fake.reserve("Guy Ritchie")
        logger.info("Fake: The book successfully reserved")
        assert result is True
        assert book_fake.issued_to == "James Bond"
        assert book_fake.reserved_by == "Guy Ritchie"

    def test_cancel_reserve_same_reader_fake(self, book_fake):
        book_fake.reserve("James Bond")
        result = book_fake.cancel_reserve("James Bond")
        logger.info("Fake: The book successfully cancelled")
        assert result is True
        assert book_fake.reserved_by is None

    def test_cancel_reserve_different_reader_fake(self, book_fake):
        book_fake.reserve("James Bond")
        result = book_fake.cancel_reserve("Guy Ritchie")
        logger.info("Fake: Reservation cannot be cancelled")
        assert result is False
        assert book_fake.reserved_by == "James Bond"

    def test_cancel_reserve_no_reservation_fake(self, book_fake):
        result = book_fake.cancel_reserve("James Bond")
        logger.info("Fake: Reservation cannot be cancelled")
        assert result is False
        assert book_fake.reserved_by is None

    def test_get_book_free_fake(self, book_fake):
        result = book_fake.get_book("James Bond")
        logger.info("Fake: Free book has been issued")
        assert result is True
        assert book_fake.issued_to == "James Bond"

    def test_get_book_reserved_by_same_reader_fake(self, book_fake):
        book_fake.reserve("James Bond")
        result = book_fake.get_book("James Bond")
        logger.info("Fake: Reserve book has been issued")
        assert result is True
        assert book_fake.reserved_by is None
        assert book_fake.issued_to == "James Bond"

    def test_get_book_reserved_by_different_reader_fake(self, book_fake):
        book_fake.reserve("James Bond")
        result = book_fake.get_book("Guy Ritchie")
        logger.info("Fake: The book already reserved different reader")
        assert result is False
        assert book_fake.reserved_by == "James Bond"
        assert book_fake.issued_to is None

    def test_get_book_issued_book_fake(self, book_fake):
        book_fake.get_book("James Bond")
        result = book_fake.get_book("Guy Ritchie")
        logger.info("Fake: The book was issued")
        assert result is False
        assert book_fake.issued_to == "James Bond"

    def test_return_book_same_reader_fake(self, book_fake):
        book_fake.get_book("James Bond")
        result = book_fake.return_book("James Bond")
        logger.info("Fake: The book was returned")
        assert result is True
        assert book_fake.issued_to is None

    def test_return_book_not_issued_fake(self, book_fake):
        result = book_fake.return_book("James Bond")
        logger.info("Fake: The book was not issued")
        assert result is False
        assert book_fake.issued_to is None

    def test_book_stub(self, book_stub):
        assert book_stub.book_name == "The Book"
        assert book_stub.author == "The Author"
        assert book_stub.num_pages == 10
        assert book_stub.isbn == "123"
        logger.info("Stub: The book are correct")

    def test_reserve_mock(self, mocker):
        mock_book = mocker.Mock()
        mock_book.reserve.return_value = True
        result = mock_book.reserve("James Bond")
        mock_book.reserve.assert_called_once_with("James Bond")
        assert result is True
        logger.info("Mock: Reserve the book")

    def test_get_book_called_correctly_mock(self, mocker):
        mock_book = mocker.Mock()
        mock_book.get_book.return_value = True
        result = mock_book.get_book("James Bond")
        mock_book.get_book.assert_called_once_with("James Bond")
        assert result is True
        logger.info("Mock: Get the book")

    def test_return_book_not_issued(self, mocker):
        mock_book = mocker.Mock()
        mock_book.return_book.return_value = False
        result = mock_book.return_book("James Bond")
        mock_book.return_book.assert_called_once_with("James Bond")
        assert result is False
        logger.info("Mock: Return the book")

    def test_cancel_reserve_mock(self, mocker):
        mock_book = mocker.Mock()
        mock_book.cancel_reserve.return_value = True
        result = mock_book.cancel_reserve("James Bond")
        mock_book.cancel_reserve.assert_called_once_with("James Bond")
        assert result is True
        logger.info("Mock: Cancel the reserved book")

    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_unstable_book_reservation(self, book_fake):
        time.sleep(random.uniform(0.1, 0.4))

        if random.random() < 0.3:
            logger.info("Unstable test: Skipped")
            assert False

        result = book_fake.reserve("James Bond")
        assert result is True
        logger.info("Unstable test: PASSED")

    def test_real_book_reservation(self, book):
        result = book.reserve("James Bond")
        assert result is True
        logger.info("Real book reservation: PASSED")
