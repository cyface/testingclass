from unittest.mock import patch, MagicMock

import responses
from django.test import TestCase

from todo.photo_api import get_photo_url_for_id


class TestPhotoApi(TestCase):
    """
    Test the Photo API
    """

    def test_photo_api(self):
        result = get_photo_url_for_id(1)
        self.assertEqual(result, 'https://via.placeholder.com/150/92c952', "Photo URL Did Not Match")

    def test_photo_api_mock(self):
        with patch('todo.photo_api.get_photo_url_for_id', MagicMock(return_value='https://via.placeholder.com/150/92c952')):
            result = get_photo_url_for_id(1)
            self.assertEqual(result, 'https://via.placeholder.com/150/92c952', "Photo URL Did Not Match")

    def test_photo_api_response_mock(self):
        with responses.RequestsMock() as resp_mock:
            resp_mock.add(resp_mock.GET, 'https://jsonplaceholder.typicode.com/photos/1', json={"thumbnailUrl": "https://via.placeholder.com/150/92c952"})
            result = get_photo_url_for_id(1)
            self.assertEqual(result, 'https://via.placeholder.com/150/92c952', "Photo URL Did Not Match")
