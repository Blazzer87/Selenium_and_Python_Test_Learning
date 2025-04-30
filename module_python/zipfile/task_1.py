import os
from zipfile import ZipFile


file_list = ['to_archive_1.txt', 'to_archive_2.txt', 'to_archive_3.txt']

def add_to_zip():
    if os.path.isfile("to_archive.zip") is True:
        os.remove("to_archive.zip")
        print("файл удалён")
        assert os.path.isfile("to_archive.zip") == False
    with ZipFile("to_archive.zip", "a") as zip:
            for i in file_list:
                zip.write(i)
            print("файл сгенерирован")
    assert os.path.isfile("to_archive.zip") == True



def find_all_files():
    print(os.path.join(os.getcwd(), r'\allure-results'))
    print(os.listdir(os.path.join(os.getcwd(),r'\allure-results')))


find_all_files()

def get_path():
    print(os.getcwd())

get_path()