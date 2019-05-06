"""
Tests
"""
from django.test import TestCase


class HomePageTest(TestCase):
    """
    Tests for Home Page
    """

    def test_home_page_loads(self):
        home_page_result = self.client.get('/')
        self.assertContains(home_page_result, 'Home')
