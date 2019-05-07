from django.test import TestCase
from django.template import Context, Template

from todo.models import List
from todo.photo_api import get_photo_url_for_id


class TestListModel(TestCase):
    """
    Test the List Model
    """

    @classmethod
    def setUpTestData(cls):
        cls.list1 = List(name="Test List 1")
        cls.list2 = List(name="Test List 2")

    def test_list_data(self):
        test_lists = List.objects.all()
        #self.assertEqual(len(test_lists), 2)

        #test_list_1 = List.objects.get(pk=1)
        #self.assertEqual(test_list_1.name, 'Test List 1')
