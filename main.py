# ************************

def ex1():
    countries = {"England": "London",
                 "Russia": "Moscow",
                 "USA": "Washington",
                 "China": "Peking",
                 "Belarus": "Minsk",
                 "Japan": "Tokyo",
                 "Germany": "Berlin",
                 "Poland": "Warsaw"}

    print(countries)
    country_key = input("Which country's capital do you go to find out?\n")
    print(countries[country_key])
    countries_sort = list(countries)
    countries_sort.sort()
    print(countries_sort)

# ************************


def ex2(word):
    alphabet = {"а": 1, "в": 1, "е": 1, "и": 1, "н": 1, "о": 1, "р": 1, "с": 1, "т": 1,
                "д": 2, "к": 2, "л": 2, "м": 2, "п": 2, "у": 2,
                "б": 3, "г": 3, "ё": 3, "ь": 3, "я": 3,
                "й": 4, "ы": 4,
                "ж": 5, "з": 5, "х": 5, "ц": 5, "ч": 5,
                "ш": 8, "э": 8, "ю": 8,
                "ф": 10, "щ": 10, "ъ": 10}
    point = 0

    for i in word:
        point += alphabet[i]

    print("Ваше слово стоит ", point, " очков")

# ************************


ex1()
ex2(list(input("Введите слово:\n")))
