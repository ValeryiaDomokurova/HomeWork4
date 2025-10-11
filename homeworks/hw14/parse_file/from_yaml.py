import yaml


def add_book(title, author, year, filename):
    books = read_books(filename)
    new_book = {
        'author': author,
        'title': title,
        'year': year
    }
    books.append(new_book)
    save_books(filename, books)


def save_books(filename, books):
    with open(filename, 'w', encoding='utf-8') as f:
        yaml.dump({'books': books}, f, allow_unicode=True)


def read_books(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data.get('books', []) if data else []
