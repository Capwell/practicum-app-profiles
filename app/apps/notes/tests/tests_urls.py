from django.test import Client

from .fixtures import Settings


class ArticleURLTests(Settings):
    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(ArticleURLTests.user_one)

    # Common page
    def test_home_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Autorized pages
    def test_add_article_url_exists_at_desired_location(self):
        response = self.authorized_client.get('/article/add/')
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url_exists_at_desired_location_authorized(self):
        response = self.authorized_client.get('/article/list/')
        self.assertEqual(response.status_code, 200)

    # Redirects for anonymous client
    def test_add_article_url_redirect_anonymous_on_admin_login(self):
        response = self.client.get('/article/add/', follow=True)
        self.assertRedirects(
            response, '/auth/login/?next=/article/add/')

    def test_articles_list_url_redirect_anonymous_on_admin_login(self):
        response = self.client.get('/article/list/', follow=True)
        self.assertRedirects(
            response, ('/auth/login/?next=/article/list/'))

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            'notes/home.html': '/',
            'notes/add_article.html': '/article/add/',
            'notes/articles_list.html': '/article/list/',
        }
        for template, url in templates_url_names.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(response, template)
