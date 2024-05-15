import pytest
from main import BooksCollector


@pytest.fixture
def book():
    return BooksCollector()

#название 40 символов
@pytest.fixture
def short_book_name():
    return 'Властелин колец The Lord of the Rings RU'

#название более 40 символов
@pytest.fixture
def long_book_name():
    return 'Властелин колец: Братство кольца 2001 (англ. The Lord of the Rings: The Fellowship of the Ring)'

@pytest.fixture
def few_books():
    return ['Властелин колец The Lord of the Rings RU', 'Озарк', 'The Last of Us']

@pytest.fixture
def few_books_genre():
    return {
            'Властелин колец The Lord of the Rings RU': 'Фантастика',
            'Озарк': 'Детективы',
            'The Last of Us': 'Ужасы'
        }

@pytest.fixture
def books_for_all_genre():
    return {
        'Властелин колец The Lord of the Rings RU': 'Фантастика',
        'Озарк': 'Детективы',
        'The Last of Us': 'Ужасы',
        'Рик и Морти': 'Мультфильмы',
        'Мальчишник в Вегасе': 'Комедии'
    }
