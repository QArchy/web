from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # отслеживается переход на главную страницу
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create')
]