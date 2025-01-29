"""
Установить виртуальное окружение
python -m venv .venv

Активировать виртуальное окружение
.venv\Scripts\activate.ps1

После этого можно переключить интерпретатор на внутренний из виртуального окружения
Existing -> VirtualEnv

Установить библиотеки, набор будет меняться, перечислены наиболее используемые
pip install pytest pydantic requests Faker python-dotenv allure-pytest

Скопировать все установленные библиотеки в файл requirements
pip freeze > requirements.txt

Скачать все библиотеки из requirements
pip install -r requirements.txt

Инициация нового GIT репозитория через консоль
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin # здесь ссылка на репозиторий https://github.com/Blazzer87/AO_Reestr.git
git push -u origin main


запуск пайтеста с аллюр отчётами
pytest --alluredir=allure-results

выгрузить отчёт на веб-морду
allure serve allure-results





"""