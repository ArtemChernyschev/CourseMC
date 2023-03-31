# Напишите функцию, которая возвращает список с уникальными (не повторяющихся) элементам.
# Не используй set, или другие функции для получения уникальных фильмов

def unique_tsil(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
numbers = list(map(int, input("Введите элементы списка: ").split()))


def main():
    unique_tsil(numbers)
    print(unique_tsil(numbers))


if __name__ == "__main__":
    main()