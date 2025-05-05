# def my_decorator(func):
#     def wrapper():
#         print("Что-то происходит перед вызовом функции.")
#         func()
#         print("Что-то происходит после вызова функции.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Привет!")
#
# say_hello()


def func_show(func):
    def qqq(*args):
        ans = func(*args)
        print("это декоратор qqq", ans)

    return qqq


@func_show
def get_sq(width=8, height=11):
    ans = width * height
    return ans


get_sq()