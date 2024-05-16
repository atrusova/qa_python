# qa_python
#### Тесты для метода add_new_book
*test_add_new_book_short_name_book_added_without_genre*
1. Проверка добавления книги (книга присутствует в списке)
2. Проверка отсутствия жанра (значение с жанром - пустое)

*test_add_new_book_when_len_more_than40_not_in_list*
Проверка что книга с названием более 40 символов не добавляется в список

#### Тест для метода set_book_genre
*test_set_book_genre_name_and_genre_exist_genre_set*
Проверка назначения жарна для книги (добавление книги, назначение жанра)

#### Тест для метода get_book_genre
*test_get_book_genre_exist_name_get_genre*
Проверка получения жанра по названию книги

#### Тест для метода get_books_with_specific_genre
*test_get_books_with_specific_genre_exist_genre_get_book_name*
Проверка вывода книги по жанру (для каждого существующего жанра)

#### Тест для метода get_books_genre
*test_get_books_genre_few_books_get_genre*
Заранее заполнили словарь и проверили получение словаря с такими же данными

#### Тест для метода get_books_for_children
*test_get_books_for_children_add_different_genre_get_correct_book*
Заранее заполнили словарь, в котором есть жарны подходящие и не подходище детям, и проверили, что метод вернул  жанр подходящий детям

#### Тест для метода add_book_in_favorites
*test_add_book_in_favorites_send_exist_book_get_book*
Добавили книгу, добавили созданную книгу в избранное, проверили что метод вернул добавленную книгу из избранного

#### Тест для метода delete_book_from_favorites
*test_delete_book_from_favorites_delete_exist_book_get_two_books*
Заранее заполнили список избранных книг, удалили одну книгу из избранного, проверили что в избранном остались все книги кроме удаленной

#### Тест для метода get_list_of_favorites_books
*test_get_list_of_favorites_books_add_favorites_books_get_list*
Добавили книгу в список, добавили книгу в избранное, проверили что списке избранных книг есть добавленная книга


