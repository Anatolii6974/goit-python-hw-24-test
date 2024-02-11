Домашнє завдання #14
HM13-MAIL-2
git clone [your-repository-link]
cd [your-project-name]
poetry install

Документування коду проекту а допомогою Sphinx
poetry add sphinx -G dev
poetry run sphinx-quickstart docs
 > docs/conf.py
Описуємо структуру документації
 > docs/index.rst
Додаємо docstrings
 > poetry run ./make.bat html
Результатом виконання команди - > docs/_build/html/index.html 

Модульні тести для репозиторію
src/repository/contacts.py:
tests/test_unit_repository_contacts.py
test_unit_repository_users.py


Функціональні тести (фреймворк pytest).
poetry add pytest
poetry add httpx -G test

conftest.py
test_route_auth.py



Для роботи проекта необхідний файл ./.env зі змінними оточення. Створіть його з таким вмістом і підставте свої значення.

poetry run docker-compose up -d
poetry run uvicorn main:app --host localhost --port 8000 --reload






