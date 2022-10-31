from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='home'),  # отслеживается переход на главную страницу
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('question/<int:question_id>', views.question, name='question')
]
