"""Задача 1: Проверка палиндрома
Напишите функцию is_palindrome(s: str) -> bool, которая принимает строку и возвращает True, если строка является палиндромом (читается одинаково слева направо и справа налево), и False в противном случае.
Игнорируйте пробелы и регистр."""


def is_palindrome(str: str) -> bool:
    pal1 = []
    for i in str:
        if i == " ":
            continue
        pal1.append(i.lower())
    x = 0
    y = 0
    pal2 = []
    while x < len(pal1):
        y -= 1
        pal2.append(pal1[y])
        x += 1
    return pal1 == pal2

is_palindrome("Hello")


print(is_palindrome("A man a plan a canal Panama"))
assert is_palindrome("A man a plan a canal Panama") == True

print(is_palindrome("Hello"))
assert is_palindrome("Hello") == False

