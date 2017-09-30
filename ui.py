from book import BookSQLData
from datetime import datetime
b1 = BookSQLData('database.db')


def add():
    book = {}
    book['name'] = input("Podaj nazwę: ")
    book['author'] = input("Podaj autora: ")
    b1.add(**book)
    run_app()


def update():
    update = {}
    update['id'] = int(input("Podaj Id książki do modyfikacji"))
    update['name'] = input("Podaj nową nazwę. Jeśli bez zmian wciśnij enter. ")
    update['author'] = input("Podaj nowego autora. Jeśli bez zmian wciśnij enter. ")
    print(update)
    b1.update(**update)
    run_app()


def book():
    b1.book('ksiadz')
    run_app()


def del_book():
    run_app()


def list():
    print(b1.list())
    choice = input("Wybierz czy chcesz zabookwoać książkę, usunąć czy zmodyfikować. Komendy: 'book', 'update', 'del'")
    if choice == 'update':
        update()
    elif choice == 'book':
        book()
    elif choice == 'del':
        del_book()


def run_app():
    options = input("Wybierz opcje z: add, list, exit: ")
    if options == 'add':
        add()
    elif options == 'list':
        list()
    elif options == 'exit':
        return None
    else:
        print("Zły wybór. Proszę wybrać z: 'add', 'list'")


if __name__ == '__main__':
    run_app()
