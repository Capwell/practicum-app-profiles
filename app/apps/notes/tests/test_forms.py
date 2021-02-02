from django.test import Client
from django.urls import reverse

from notes.models import Article

from .fixtures import Settings


class ArticleCreateFormTest(Settings):
    def setUp(self):
        self.auth_client = Client()
        self.auth_client.force_login(ArticleCreateFormTest.user_two)

    def test_create_article(self):
        articles_count = Article.objects.count()

        form_data = {
            'text': 'Тестовый текст из формы',
        }
        response = self.auth_client.post(
            reverse('notes:add_article'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, reverse('notes:home'))
        self.assertEqual(Article.objects.count(), articles_count + 1)
        self.assertTrue(Article.objects.filter(
                text='Тестовый текст из формы').exists())

    def test_cant_create_empty_article(self):
        articles_count = Article.objects.count()
        form_data = {
            'text': '&nbsp;',
        }
        response = self.auth_client.post(
            reverse('notes:add_article'),
            data=form_data,
            follow=True
        )
        self.assertEqual(Article.objects.count(), articles_count)
        self.assertFormError(
            response,
            'form',
            'text',
            'Заметка не может быть пустой.'
        )
        self.assertEqual(response.status_code, 200)

    def test_text_is_required(self):
        articles_count = Article.objects.count()
        form_data = {
            'text': '  ',
        }
        response = self.auth_client.post(
            reverse('notes:add_article'),
            data=form_data,
            follow=True
        )
        self.assertEqual(Article.objects.count(), articles_count)
        self.assertFormError(
            response,
            'form',
            'text',
            'Обязательное поле.'
        )
        self.assertEqual(response.status_code, 200)
