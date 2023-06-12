# Python_blog
Приложение личного блога. Написание постов осуществляется в панели администратора. Для редактирования контента используется редактор CKEditor-5. Так же блог оснащен строкой поиска по постам и облаком тегов.

## Стек используемых технологий.
1. Python 3.10
2. Django 4.1.7
3. PostgreSQL
4. Docker
5. Bootstrap 5.1
6. HTML5
7. HTMX
8. CSS

### Установка приложения.

1. Клонировать репозиторий.
2. Зайти в директорию "python_blog".
3. Выполнить команду ```docker-compose build```
4. Выполнить ```docker-compose up```
5. Открыть второе окно терминала в нем выполнить ряд команд ```sudo docker-compose run --rm web sh -c "python3 manage.py migrate"```
6. ```sudo docker-compose run --rm web sh -c "python3 manage.py createsuperuser"```
7. ```sudo docker-compose run --rm nginx sh -c "chmod -R 777 /var/html/"```
8. ```sudo docker-compose run --rm web sh -c "python3 manage.py collectstatic"```
9. В первом окне терминала перезапустить doker-контейнеры.

### Использование

1. Зпустить приложение в браузере по адрессу http://127.0.0.1:8000/
2. Вход в панель администратора http://127.0.0.1:8000/admin/

### Как пользоваться генератором постов для заполнения БД
1. ```python3 manage.py shell```
2. ```from blog.factory import PostFactory```
3. ```x = PostFactory.create_batch(100)```
4. ```exit()```

