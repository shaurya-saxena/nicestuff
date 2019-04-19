from django.urls import path
from django.views.generic.base import TemplateView # new

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('history', TemplateView.as_view(template_name='history.html'), name='history'),
    path('favorites', TemplateView.as_view(template_name='favorites.html'), name='favorites'),

]


