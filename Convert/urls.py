from .views import ask_page, result_page, weigth_page, temperature_page
from django.urls import path

urlpatterns = [
    path('', ask_page, name='index'),
    path('weight/', weigth_page, name='weight'),
    path('temperature/', temperature_page, name='temperature'),
    path('result/', result_page, name='result'),
]