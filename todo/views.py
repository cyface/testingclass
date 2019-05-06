"""
Views
"""
from django.views.generic import ListView, DetailView, UpdateView

from todo.forms import ItemEditForm
from todo.models import List, Item


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(UpdateView):
    form_class = ItemEditForm
    model = Item


class ListListView(ListView):
    model = List


class ListDetailView(DetailView):
    model = List
