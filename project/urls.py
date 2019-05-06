"""
URL Configuration
"""
from django.contrib import admin
from django.urls import path

from project.views import HomePageView
from todo.views import ListListView, ListDetailView, ItemDetailView, ItemUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('lists', ListListView.as_view(), name='list_list'),
    path('lists/<int:pk>/', ListDetailView.as_view(), name='list_detail'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_update'),
    path('admin/', admin.site.urls),
]
