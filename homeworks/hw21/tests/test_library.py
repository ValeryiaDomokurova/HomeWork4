import pytest
import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, level="INFO")

from homeworks.hw21.source.library.book import Book

class TestBook:

    @pytest.fixture
    def book(self):
        book = Book("The Hobbit", "J. R. R. Tolkien", 310, "0345339681")
        logger.debug("Book created")
        return book

    def test_reserve_free(self, book):
        result = book.reserve("James Bond")
        logger.info("Reserve the book")
        assert result == True
