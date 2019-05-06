"""
Django Template Tags
"""

from django import template
from todo.photo_api import get_photo_url_for_id

register = template.Library()


@register.simple_tag
def get_photo_url(id_to_fetch):
    return get_photo_url_for_id(id_to_fetch)
