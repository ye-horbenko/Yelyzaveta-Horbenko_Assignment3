book_profile = {
    "title": "Основи програмування",
    "author": "Іван Петренко",
    "year": 2023,
    "publisher_info": {
        "name": "Наукова думка",
        "city": "Київ"
    }
}

name = book_profile["title"]
author = book_profile["author"]
print(f"Назва: {name}, автор: {author}")

publisher = book_profile["publisher_info"]["name"]
print(f"Видавництво: {publisher}")

print(f"Книга '{name}' автора {author} була видана у місті {book_profile["publisher_info"]["city"]}")

if book_profile["year"]:
    print(book_profile["year"])
else:
    print("Рік видання невідомий")