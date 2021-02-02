from django.core.exceptions import ValidationError

from notes.models import Article

from .fixtures import Settings


class ArticleModelTest(Settings):
    def test_verbose_name(self):
        article = ArticleModelTest.article1
        field_verboses = {
            'text': 'Заметка',
            'author': 'Автор',
            'created_on': 'Создано',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    article._meta.get_field(value).verbose_name, expected)

    def test_validaiton_text_field_fail(self):
        article_invalid = Article.objects.create(
            text=' ',
            author=ArticleModelTest.user_two,
        )
        with self.assertRaises(ValidationError):
            article_invalid.full_clean()
            article_invalid.save()
