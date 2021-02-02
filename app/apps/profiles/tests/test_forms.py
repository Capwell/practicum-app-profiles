from django.urls import reverse

from profiles.models import User

from .fixtures import Settings


class UserCreateFormTest(Settings):
    def test_create_user(self):
        users_count = User.objects.count()
        form_data = {
            'email': 'test_user@py.py',
            'password1': 'eGfolh4jhsaKsd3',
            'password2': 'eGfolh4jhsaKsd3',
        }
        response = self.client.post(
            reverse('profiles:registration'),
            data=form_data,
            follow=True
        )
        self.assertTrue(User.objects.filter(
                email='test_user@py.py').exists())
        user = response.context.get('user')
        self.assertEqual(user, User.objects.get(email='test_user@py.py'))
        self.assertEqual(User.objects.count(), users_count + 1)
        self.assertRedirects(response, reverse('profiles:profile'))

    def test_cant_create_user_with_existing_emali(self):
        users_count = User.objects.count()
        form_data = {
            'email': '3@py.py',
        }
        response = self.client.post(
            reverse('profiles:registration'),
            data=form_data,
            follow=True
        )
        self.assertFormError(
            response,
            'form',
            'email',
            'Профиль с таким Email уже существует.'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), users_count)
