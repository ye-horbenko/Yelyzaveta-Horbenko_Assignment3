book_profiles = [
    {
        "title": "Основи програмування",
        "author": "Іван Петренко",
        "year": 2023,
        "rating": 6.0,
        "publisher_info": {
            "name": "Наукова думка",
            "city": "Київ"
        }
    },
    {
        "title": "Гаррі Поттер і Келих вогню",
        "author": "Дж. К. Роулінг",
        "year": 2000,
        "rating": 9.9,
        "publisher_info": {
            "name": "Bloomsbury",
            "city": "Лондон"
        }
    }
]

for book in book_profiles:
    title = book["title"]
    author = book["author"]
    print(f"Назва: {title}")
    print(f"Автор: {author}")

    publisher = book["publisher_info"]["name"]
    print(f"Видавництво: {publisher}")

    city = book["publisher_info"]["city"]
    print(f'Книга "{title}" автора {author} була видана у місті {city}.')

    if "year" in book:
        print(f"Рік видання: {book['year']}")
    else:
        print("Рік видання невідомий")

rating = float(input("What is your expected rating? "))
if rating > book_profiles[0]["rating"]:
    print(f"Perfect book for you is {book_profiles[1]["title"]}")
else:
    print(f"You might like '{book_profiles[0]["title"]}', "
          f"though we would still recommend '{book_profiles[1]["title"]}'")