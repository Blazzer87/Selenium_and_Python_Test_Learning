from zipfile import ZipFile

import pytest


# @pytest.fixture(autouse=True)
# def create_zip():
#     ZipFile("to_archive_1.zip", "w")      # создаём пустой архив
#

def add_to_zip():
    ZipFile("to_archive_1.zip", "w").write('to_archive_1.txt')

add_to_zip()