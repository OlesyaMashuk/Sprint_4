
import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1.тесты метода add_new_book 
    @pytest.mark.parametrize("name, expected_success", [("Овод", True),("", False),("А" * 40, True),("А" * 41, False)])
    def test_add_new_book(self, name, expected_success):
        collector = BooksCollector()
        # название книги должно быть корректным 
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected_success

    # Одну и ту же книгу нельзя добавить дважды
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Поющие в терновнике")
        collector.add_new_book("Поющие в терновнике")
        assert len(collector.get_books_genre()) == 1


    # 2. тесты метода set_book_genre
    @pytest.mark.parametrize("book_name, genre, expected_genre",[("Убийство в Восточном экспрессе", "Детективы", "Детективы"), ("Дракула", "Ужасы", "Ужасы"),("Двенадцать стульев", "Комедии", "Комедии")])
    def test_set_book_genre(collector, book_name, genre, expected_genre):
        collector = BooksCollector()
        # установка жанра книги, она должна быть в books_genre
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

        # установка жанра для несуществующей книги
    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre("Книга не существует", "Ужасы")
        assert "Книга не существует" not in collector.books_genre    


    # 3. тест метода get_book_genre
    # получение жанра книги по ее имени
    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Отцы и дети")
        collector.set_book_genre("Отцы и дети", "Детективы")
        assert collector.get_book_genre("Отцы и дети") == "Детективы"

        
    # 4. тест для метода get_books_with_specific_genre
    # получение списка книг определенного жанра
    def test_get_books_with_specific_multiple(self):
        collector = BooksCollector()
        collector.add_new_book("Марсианин")
        collector.add_new_book("Интерстеллар")
        collector.add_new_book("Оно")
        
        collector.set_book_genre("Марсианин", "Фантастика")
        collector.set_book_genre("Интерстеллар", "Фантастика")
        collector.set_book_genre("Оно", "Ужасы")

        sci_fi_books = collector.get_books_with_specific_genre("Фантастика")
        assert len(sci_fi_books) == 2
        assert "Марсианин" in sci_fi_books
        assert "Интерстеллар" in sci_fi_books

    # 5. тест для метода get_books_genre
    # выводим словарь со всеми книгами и их жанрами
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Интерстеллар")
        collector.set_book_genre("Интерстеллар", "Фантастика")
        collector.add_new_book("Отцы и дети")
        collector.set_book_genre("Отцы и дети", "Детективы")

        result = collector.get_books_genre()
        assert isinstance(result, dict)
        assert result == {"Интерстеллар": "Фантастика", "Отцы и дети": "Детективы"}

    # 6. тест для метода get_books_for_children
    # книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_get_books_for_children_empty(self):
        collector = BooksCollector()
        collector.add_new_book("Страшная книга")
        collector.set_book_genre("Страшная книга", "Ужасы")
        assert collector.get_books_for_children() == []


    # 7. тесты для метода add_book_in_favorites
    # Успешное добавление книги в избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Щелкунчик")
        collector.add_book_in_favorites("Щелкунчик")
        
        assert "Щелкунчик" in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1 

    # Повторно добавить книгу в избранное нельзя
    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        assert collector.favorites.count("Мастер и Маргарита") == 1 

    # 8. тест метода delete_book_from_favorites
    # успешное удаление книги из избранного
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Библия")
        collector.add_book_in_favorites("Библия")
        collector.delete_book_from_favorites("Библия")
        assert "Библия" not in collector.get_list_of_favorites_books()

    # 9. тест метода get_list_of_favorites_books
    # получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга_1")
        collector.add_new_book("Книга_2")
        collector.add_new_book("Книга_3")

        collector.add_book_in_favorites("Книга_1")
        collector.add_book_in_favorites("Книга_3")

        result = collector.get_list_of_favorites_books()
        assert isinstance(result, list)
        assert result == ["Книга_1", "Книга_3"]


