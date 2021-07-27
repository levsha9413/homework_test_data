'''
1.Распарсить нужные поля из user.json
    1.1 Используем менеджер контекста для открытия файла
    1.2 Используем генераторы для чтения файла
    1.3 Куда-то складываем результат
2.Распарсить нужные поля из books.csv
    2.1 Используем менеджер контекста для открытия файла
    2.2 Используем генераторы для чтения файла
    2.3 Куда-то складываем результат
3.Склеить их и положить в  result.json
4.Добавить src/ в gitignore
'''

# добавить src/ в gitignore

import json
from csv import DictReader





def book_parser():
    with open("./src/books.csv", "r") as csv_file:
        books = DictReader(csv_file)
        for book in books:
            books_fields = {}
            books_fields["title"] = book["Title"]
            books_fields["author"] = book["Author"]
            books_fields["pages"] = book["Pages"]
            books_fields["genre"] = book["Genre"]
            yield books_fields

book_fields = book_parser()




with open("./src/users.json", "r") as json_file:
    users = (i for i in (json.loads(json_file.read())))
    result = []

    for user in users:
        parse_data = {}
        parse_data["name"] = user["name"]
        parse_data["gender"] = user["gender"]
        parse_data["address"] = user["address"]
        parse_data["age"] = user["age"]
        parse_data["books"] = [next(book_fields)]
        result.append(parse_data)

with open("./result.json", "w") as json_result:
    json.dump(result, json_result, indent=4)
