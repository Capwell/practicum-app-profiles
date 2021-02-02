import datetime

from django.contrib.auth import get_user_model
from django.db import transaction
from django.test import TestCase

from notes.forms import ArticleCreateForm
from notes.models import Article


class Settings(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user = get_user_model()
        cls.user_one = user.objects.create_user(email='1@py.py', password='1')
        cls.user_two = user.objects.create_user(email='2@py.py', password='1')
        cls.article1 = Article.objects.create(
            id=1,
            text='Тестовый текст1',
            author=cls.user_one,
            created_on=datetime.date.today(),
        )
        cls.article2 = Article.objects.create(
            id=2,
            text='Тестовый текст2',
            author=cls.user_one,
            created_on=datetime.date.today() + datetime.timedelta(days=1),
        )
        cls.article3 = Article.objects.create(
            text='Тестовый текст',
            author=cls.user_two,
        )
        cls.form = ArticleCreateForm()
