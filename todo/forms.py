"""
Django Forms
"""
from django.forms import ModelForm

from todo.models import Item


class ItemEditForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['pk']
