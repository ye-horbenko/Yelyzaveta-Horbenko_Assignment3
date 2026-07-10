book_profile = {
    "title": "Основи програмування",
    "author": "Іван Петренко",
    "year": 2023,
    "publisher_info": {
        "name": "Наукова думка",
        "city": "Київ"
    }
}

print(book_profile["title"])
print(book_profile["author"])

print(book_profile["publisher_info"]["name"])

print(f"Книга '{book_profile["publisher_info"]["name"]}' автора була видана у місті "
      f"{book_profile["publisher_info"]["city"]}")

if book_profile["year"]:
    print(book_profile["year"])
else:
    print("Рік видання невідомий")