# School Media Center (Django)

## Что есть
- Авторизация и регистрация (пользователь / админ)
- Новостная лента (статьи):
  - пользователь: создаёт и редактирует **свои** статьи
  - администратор: может делать то же + **удалять** любые статьи
- Фото-галерея:
  - папки + загрузка фото (доступно только авторизованным пользователям)
- Видео: список (добавление через админку)

## Запуск
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/
Админка: http://127.0.0.1:8000/admin/

## Страницы
- Вход: `/login/`
- Регистрация: `/register/`
- Новости: `/posts/`
- Фото: `/gallery/`
- Видео: `/videos/`

