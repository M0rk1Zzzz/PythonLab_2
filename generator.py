import random, csv

def generator(output = 'output.txt'):
    with open('books-en.csv', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        list_reader = list(reader)
        random_lines = random.sample(list_reader, 20)
    
    with open(output, 'w', encoding='utf-8') as output_file:
        for number, row in enumerate(random_lines, 1):
            author = row['Book-Author']
            title = row['Book-Title']
            year = row['Year-Of-Publication']
            output_file.write(f"{number}. {author}. {title} - {year}\n")

generator()

        

