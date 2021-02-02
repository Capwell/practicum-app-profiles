# Приложение для демонстрации расширенной модели пользователя

Стек
Django
PostgreSQL
bootstrap4


### Деплой

Использован gunicorn + nginx.

1. Переименуйте *.env.prod-sample* в *.env.prod*,
а *.env.prod.db-sample* в *.env.prod.db*.
2. При необходимости обновите пременные окружения.
3. Создайте образ, проведите миграции и запустите.

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml up
```

Проект будет доступен по адресу [http://localhost:4000](http://localhost:4000)
