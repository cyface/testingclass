"""
Views
"""
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "project/home_page.html"
