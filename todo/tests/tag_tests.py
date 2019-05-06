from django.test import TestCase
from django.template import Context, Template

from todo.models import List
from todo.photo_api import get_photo_url_for_id


class TestPhotoTag(TestCase):
    """
    Test the Photo Tag
    """

    def test_get_photo_tag(self):
        template = Template("{% load todo_tags %}{% get_photo_url 1 %}")
        result = template.render(Context())
        self.assertIn('https://via.placeholder.com/150/92c952', result)
