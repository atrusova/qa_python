import pytest
from main import BooksCollector

@pytest.fixture
def book():
    return BooksCollector()
