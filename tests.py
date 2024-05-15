import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_short_name_book_added_without_genre(self, book, short_book_name):
        book.add_new_book(short_book_name)
        assert short_book_name in book.books_genre and len(book.books_genre.values()) <= 1

    @pytest.mark.parametrize('name',
        [
            'Властелин колец: Братство Кольца (англ. The Lord of the Rings: The Fellowship of the Ring)',
            'Властелин колец: 2 крепости (англ. The Lord of the Rings: The Two Towers)'
        ]
    )
    def test_add_new_book_when_len_more_than40_not_in_list(self, book, name):
        book.add_new_book(name)
        assert name not in book.books_genre

    def test_set_book_genre_name_and_genre_exist_genre_set(self, book, short_book_name):
        book.add_new_book(short_book_name)
        book.set_book_genre(short_book_name, 'Фантастика')
        assert book.books_genre.get('Властелин колец The Lord of the Rings RU')

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Властелин колец The Lord of the Rings RU', 'Фантастика'],
            ['Озарк', 'Детективы'],
            ['The Last of Us', 'Ужасы']
        ]
    )
    def test_get_book_genre_exist_name_get_genre(self, book, name, genre, few_books_genre):
        book.books_genre = few_books_genre
        assert book.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Властелин колец The Lord of the Rings RU', 'Фантастика'],
            ['Озарк', 'Детективы'],
            ['The Last of Us', 'Ужасы'],
            ['Рик и Морти', 'Мультфильмы'],
            ['Мальчишник в Вегасе', 'Комедии']
        ],
        ids=[
            'Test for genre 1',
            'Test for genre 2',
            'Test for genre 3',
            'Test for genre 4',
            'Test for genre 5'
            ]
    )
    def test_get_books_with_specific_genre_exist_genre_get_book_name(self, book, books_for_all_genre, name, genre):
        book.books_genre = books_for_all_genre
        assert book.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_few_books_get_genre(self, book, few_books_genre):
        book.books_genre = few_books_genre
        assert book.get_books_genre() == few_books_genre

    def test_get_books_for_children_add_different_genre_get_correct_book(self, book, few_books_genre):
        book.books_genre = few_books_genre
        assert 'The Last of Us' not in book.get_books_for_children()

    def test_add_book_in_favorites_send_exist_book_get_book(self, book, short_book_name):
        book.add_new_book(short_book_name)
        book.add_book_in_favorites(short_book_name)
        assert book.favorites == ['Властелин колец The Lord of the Rings RU']

    def test_delete_book_from_favorites_delete_exist_book_get_two_books(self, book, few_books):
        book.favorites = few_books
        book.delete_book_from_favorites('Озарк')
        assert book.favorites == ['Властелин колец The Lord of the Rings RU', 'The Last of Us']

    def test_get_list_of_favorites_books_add_favorites_books_get_list(self, book, short_book_name):
        book.add_new_book(short_book_name)
        book.add_book_in_favorites(short_book_name)
        assert book.favorites == [short_book_name]
