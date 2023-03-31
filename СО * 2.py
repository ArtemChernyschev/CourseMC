# такие слова как первый, второй, третий являются числительными.
# В данном упражнении вам необходимо написать функцию принимающую на вход в качестве единственного аргумента целое число
# и возвращающую строковое значение содержащее соответсвующее числительное (на английском языке)
# Ваша функция должна обрабатывать числа от 1 до 12.
# Если выходящее значение выходит за границы данного диапазона, вывод должен оставаться пустым.
# В основной программе запустите цикл по натуральным числам от 1 до 12 и выведите на экран соответствующие им числительные.
# Ваша программа должна запускаться только в том случае, если не импортирована в виде модуля в другой файл


def ordinal_number(number):
    if number == 1:
        return "first"
    elif number == 2:
        return "second"
    elif number == 3:
        return "third"
    elif number == 4:
        return "fourth"
    elif number == 5:
        return "fifth"
    elif number == 6:
        return "sixth"
    elif number == 7:
        return "seventh"
    elif number == 8:
        return "eighth"
    elif number == 9:
        return "ninth"
    elif number == 10:
        return "tenth"
    elif number == 11:
        return "eleventh"
    elif number == 12:
        return "twelfth"
    else:
        return ""


def main():
    for i in range(1, 13):
        ordinal = ordinal_number(i)
        if ordinal:
            print(f'{i}: {ordinal}')


if __name__ == "__main__":
    main()