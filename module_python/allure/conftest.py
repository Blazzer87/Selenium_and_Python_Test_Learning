import os
import shutil
import requests
#
# def pytest_sessionfinish():
#
#     """Хук, выполняемый после окончания сессии, поочерёдно дёргающий каждую из функций-шагов."""
#
#     if step_1_generate_allure_report():
#         zip_report_path = step_2_archive_allure_report()
#         step_3_upload_report(zip_report_path)
#     else:
#         print("Папка 'allure-report' не найдена.")
#
#
# def step_1_generate_allure_report():
#
#     """Генерируем отчет Allure из папки allure-results."""
#
#     global path
#     path = os.getcwd()
#
#     if not os.path.isdir(os.path.join(path, 'allure-results')):
#         print("Папка 'allure-results' не найдена.")
#         return False
#
#     print("\nПапка 'allure-results' найдена. Приступаю к генерации отчёта.")
#     os.system("allure generate allure-results -c -o allure-report")
#
#     return os.path.isdir(os.path.join(path, 'allure-report'))
#
#
# def step_2_archive_allure_report():
#
#     """Создаем архив отчета Allure."""
#
#     if os.path.isfile(os.path.join(path, 'allure-report.zip')):
#         os.remove(os.path.join(path, 'allure-report.zip'))
#         print("Обнаружена предыдущая версия архива allure-report.zip. Она будет удалена.")
#
#     shutil.make_archive(base_name=os.path.join(path, "allure-report"),
#                         format="zip",
#                         root_dir=path,
#                         base_dir="allure-report")
#     print("Архив allure-report.zip успешно создан.")
#
#     return os.path.join(path, 'allure-report.zip')
#
#
# def step_3_upload_report(zip_report_path):
#
#     """Загружаем архив отчета в DoQA."""
#
#     with open(zip_report_path, mode='rb') as zip_report:
#         response = requests.post(
#             url='https://0oj975.doqa.app/api/autotests/report',
#             data={
#                 "token": "5590e9ae-a719-4b39-a059-f9a7847e958e",
#                 "type": "allure"
#             },
#             files={
#                 "file": ("allure-report.zip", zip_report, "application/zip")
#             }
#         )
#
#     if response.status_code == 200 and response.text == '"ok"':
#         print("Отчёт allure-report.zip успешно загружен в DoQA.")
#     else:
#         print("Отчёт не был загружен в DoQA.")
#
#
