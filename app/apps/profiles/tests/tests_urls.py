from django.test import Client

from .fixtures import Settings


class ProfilesURLTests(Settings):
    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(ProfilesURLTests.user_one)

    def test_urls_exists_at_desired_location(self):
        url_names = [
            '/auth/signup/',
            '/auth/logout/',
            '/auth/login/',
        ]
        for url in url_names:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_profile_url_exists_at_desired_location_authorized(self):
        response = self.authorized_client.get('/auth/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_url_redirect_anonymous_on_admin_login(self):
        response = self.client.get('/auth/profile/', follow=True)
        self.assertRedirects(
            response, '/auth/login/?next=/auth/profile/')

    def test_urls_uses_correct_template(self):
        templates_url_names = {
            'profiles/registration.html': '/auth/signup/',
            'profiles/profile.html': '/auth/profile/',
            'profiles/login.html': '/auth/login/',
            'profiles/logout.html': '/auth/logout/',
        }
        for template, url in templates_url_names.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(response, template)
