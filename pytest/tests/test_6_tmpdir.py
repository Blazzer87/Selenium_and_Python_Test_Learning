import pytest


def test_write_and_read(tmpdir):
    # Создаем временный файл
    temp_file = tmpdir.join("tempfile.txt")

    # Записываем данные в файл
    temp_file.write("Hello, pytest!")

    # Читаем данные из файла
    content = temp_file.read()

    # Проверяем, что содержимое файла соответствует ожидаемому
    assert content == "Hello, pytest!"



def test_multiple_tempdirs(tmpdir_factory):
    # Создаем временную директорию
    temp_dir = tmpdir_factory.mktemp("my_temp_dir")
    print("\n вот что возвращает getbasetemp", tmpdir_factory.getbasetemp())

    # Создаем файл в созданной директории
    temp_file = temp_dir.join("file1.txt")
    temp_file.write("Content for file 1")

    # Проверяем содержимое файла
    assert temp_file.read() == "Content for file 1"

    # Создаем еще один файл в той же временной директории
    another_file = temp_dir.join("file2.txt")
    another_file.write("Content for file 2")

    # Проверяем содержимое второго файла
    assert another_file.read() == "Content for file 2"
