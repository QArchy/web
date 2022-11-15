from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Questions_new.as_view(), name='home'),
    path('hot', Questions_hot.as_view(), name='home_hot'),
    path('login', views.login, name='login'),
    path('settings', views.settings, name='settings'),
    path('register', views.register, name='register'),
    path('user', User.as_view(), name='logged_in'),
    path('ask', views.create, name='ask'),
    path('question/<int:question_id>', Question_f.as_view(), name='question'),
    path('tag/<str:tag>', Questions_tag.as_view(), name='question_by_tag'),
]
