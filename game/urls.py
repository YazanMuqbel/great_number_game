from django.urls import path     
from . import views
urlpatterns = [
    path('', views.game, name='home_page'),
    path('guess/', views.guess_number, name='guess_number'),
    path('result/', views.guess_result, name='guess_result'),
]
