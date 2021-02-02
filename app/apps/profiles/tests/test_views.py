from django import forms
from django.test import Client
from django.urls import reverse

from .fixtures import Settings


class ProfilesPagesTests(Settings):
    def setUp(self):
        self.auth_client = Client()
        self.auth_client.force_login(ProfilesPagesTests.user_one)

    def test_pages_uses_correct_template(self):
        templates_page_names = {
            'profiles/registration.html': reverse('profiles:registration'),
            'profiles/profile.html': reverse('profiles:profile'),
            'profiles/login.html': (reverse('profiles:login')),
            'profiles/logout.html': reverse('profiles:logout'),
        }
        for template, reverse_name in templates_page_names.items():
            with self.subTest(template=template):
                response = self.auth_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_profile_receive_correct_context(self):
        response = self.auth_client.get(reverse('profiles:profile'))
        expected = response.context.get('object')
        self.assertEqual(expected, ProfilesPagesTests.user_one)

    def test_registration_receive_correct_context(self):
        response = self.auth_client.get(reverse('profiles:registration'))
        form_fields = {
            'email': forms.fields.CharField,
            'password1': forms.fields.CharField,
            'password2': forms.fields.CharField,
        }
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_field, expected)
