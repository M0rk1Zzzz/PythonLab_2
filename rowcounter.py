import csv

count = 0

with open('books-en.csv', encoding='latin-1') as csvfile:
    table = csv.DictReader(csvfile, delimiter=';')
    for row in table:
        if len(row["Book-Title"]) > 30:
            count += 1

print(count)
