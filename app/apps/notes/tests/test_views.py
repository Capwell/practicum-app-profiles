from django import forms
from django.test import Client
from django.urls import reverse

from .fixtures import Settings


class ArticlePagesTests(Settings):
    def setUp(self):
        self.auth_client = Client()
        self.auth_client.force_login(ArticlePagesTests.user_one)

    def test_pages_uses_correct_template(self):
        templates_page_names = {
            'notes/home.html': reverse('notes:home'),
            'notes/add_article.html': reverse('notes:add_article'),
            'notes/articles_list.html': reverse('notes:articles_list'),
        }
        for template, reverse_name in templates_page_names.items():
            with self.subTest(template=template):
                response = self.auth_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_home_page_receive_correct_context_anonimus(self):
        response = self.client.get(reverse('notes:home'))
        self.assertEqual(response.context.get('app_name'), 'Заметки')
        self.assertEqual(response.context.get('articles_count'), None)

    def test_home_page_receive_correct_context(self):
        response = self.auth_client.get(reverse('notes:home'))
        self.assertEqual(response.context.get('app_name'), 'Заметки')
        self.assertEqual(response.context.get('articles_count'), 2)

    def test_task_list_page_list_is_2(self):
        response = self.auth_client.get(reverse('notes:articles_list'))
        self.assertEqual(len(response.context['object_list']), 2)

    def test_articles_list_context_in_correct_order(self):
        response = self.auth_client.get(reverse('notes:articles_list'))
        first_article_in_list = response.context.get('object_list').first().id
        second_article_in_list = response.context.get('object_list').last().id
        self.assertEqual(first_article_in_list, ArticlePagesTests.article2.id)
        self.assertEqual(second_article_in_list, ArticlePagesTests.article1.id)

    def test_articles_list_receive_correct_context(self):
        response = self.auth_client.get(reverse('notes:articles_list'))
        expected_text = response.context.get('object_list')[0].text
        expected_created_on = response.context.get('object_list')[0].created_on
        self.assertEqual(expected_text,
                         ArticlePagesTests.article2.text)
        self.assertEqual(expected_created_on,
                         ArticlePagesTests.article2.created_on)

    def test_add_article_receive_correct_context(self):
        response = self.auth_client.get(reverse('notes:add_article'))
        form_fields = {
            'text': forms.fields.CharField,
        }
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_field, expected)
