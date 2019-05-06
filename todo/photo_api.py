"""
Photo API that gets URL of image for an ID number
"""
import requests

"""
Sample API Response

{
  "albumId": 1,
  "id": 1,
  "title": "accusamus beatae ad facilis cum similique qui sunt",
  "url": "https://via.placeholder.com/600/92c952",
  "thumbnailUrl": "https://via.placeholder.com/150/92c952"
}

"""


def get_photo_url_for_id(id_to_fetch):
    result = requests.get(f"https://jsonplaceholder.typicode.com/photos/{id_to_fetch}")
    if result.status_code == requests.codes.ok:
        result_obj = result.json()
        return result_obj['thumbnailUrl']
    else:
        return None
