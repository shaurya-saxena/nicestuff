from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('history', views.history, name='history'),
    path('favorites', views.favorites, name='favorites'),

]


