from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Questions_new.as_view(), name='home'),
    path('hot', Questions_hot.as_view(), name='home_hot'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('profile/edit', settings, name='settings'),
    path('signup', register, name='signup'),
    path('ask', ask, name='ask'),
    path('question/<int:question_id>', Question_f, name='question'),
    path('tag/<str:tag>', Questions_tag.as_view(), name='question_by_tag'),
]
