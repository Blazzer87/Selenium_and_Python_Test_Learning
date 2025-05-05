import os
import shutil
import requests


def pytest_sessionfinish(session, exitstatus):
    path = os.getcwd()
    if os.path.isdir(os.path.join(path, 'allure-results')):
        print("Папка 'allure-results' существует. Приступаю к генерации отчёта.")

        # отправляем команду на генерацию нового allure-report
        # удалять его предварительно не нужно, он очищается командой
        os.system("allure generate allure-results --clean -o allure-report")

        # проверяем успешность создания allure-report
        if os.path.isdir(os.path.join(path, 'allure-report')):
            print("Папка 'allure-report' сгенерирована. Приступаю к архивации отчёта.")

            # проверяем наличие устаревшего архива отчёта и удаляем его
            if os.path.isfile(os.path.join(path, 'allure-report.zip')):
                os.remove(os.path.join(path, 'allure-report.zip'))
                print("Обнаружена предыдущая версия архива allure-report.zip. Она будет удалена.")

            # создаём архив
            shutil.make_archive(base_name=os.path.join(path, "allure-report"),
                                format="zip",
                                root_dir=path,
                                base_dir="allure-report")
            print("Архив allure-report.zip успешно создан. Приступаю к отправке в DoQA.")

            zip_report_path = os.path.join(path, 'allure-report.zip')

            assert os.path.isfile(zip_report_path) == True
            with open(file=zip_report_path, mode='rb') as zip_report:
                response = requests.post(
                    url='https://0oj975.doqa.app/api/autotests/report',
                    data={
                        "token": "5590e9ae-a719-4b39-a059-f9a7847e958e",
                        "type": "allure"
                        },
                    files={
                        "file": ("allure-report.zip", zip_report, "application/zip")
                        })
            if response.status_code == 200 and response.text == "ok":
                print("Отчёт allure-report.zip успешно загружен в DoQA.")
            else:
                print("Отчёт не был загружен в DoQA.")
        else:
            print("Папка 'allure-report' не найдена.")
    else:
        print("Папка 'allure-results' не найдена.")



