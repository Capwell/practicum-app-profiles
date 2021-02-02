from profiles.models import User

from .fixtures import Settings


class ProfilesModelTest(Settings):
    def test_create_user(self):
        simple_user = User.objects.create_user(
                      email='t1@py.py', password='1')
        self.assertEqual(simple_user.is_staff, False)
        self.assertEqual(simple_user.is_active, True)
        self.assertEqual(simple_user.is_superuser, False)

    def test_create_superuser(self):
        simple_user = User.objects.create_superuser(
                      email='t2@py.py', password='1')
        self.assertEqual(simple_user.is_staff, True)
        self.assertEqual(simple_user.is_active, True)
        self.assertEqual(simple_user.is_superuser, True)
