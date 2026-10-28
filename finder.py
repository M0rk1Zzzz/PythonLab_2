import csv

def author_finder():
    with open('books-en.csv', encoding='latin-1') as csvfile:
        table = csv.DictReader(csvfile, delimiter=';')
        author_need = input('Input author, which book you need:').lower()
        books = []
        for row in table:
            author = row['Book-Author'].lower()
            book = row['Book-Title']
            price = row['Price'].replace(',', '.')
            if author_need in author and float(price) > 150:
                books.append(book)
    return books if len(books) > 0 else 'Books are not found'


print(author_finder())

