from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


# Used just for data transfer from input to User and Profile Update
class SettingsModel(models.Model):
    username = models.CharField('Login', max_length=20, blank=True)
    email = models.EmailField('Email', max_length=20, blank=True)
    first_name = models.CharField('Nickname', max_length=20, blank=True)
    avatar = models.ImageField(upload_to='main/static/img', blank=True)
###################################################################


class ProfileManager(models.Manager):
    def best(self):
        return Profile.objects.order_by('-rating')[:5]


class Profile(models.Model):
    avatar = models.ImageField(upload_to='main/static/img')
    rating = models.IntegerField('Rating', default=0, null=False)
    user_fk = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = ProfileManager()


class Question(models.Model):
    title = models.CharField('Title', max_length=50)
    descr = models.TextField('Description')
    author_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class TagManager(models.Manager):
    def popular(self):
        return Tag.objects.annotate(
            occurrences=Count('questions')
        ).order_by('-occurrences')[:5]


class Tag(models.Model):
    tag = models.CharField('Tag', max_length=50, blank=True)
    questions = models.ManyToManyField(Question)
    objects = TagManager()


class Answer(models.Model):
    descr = models.TextField('Description')
    correct = models.BooleanField(default=False)
    author_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    question_fk = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class QuestionLike(models.Model):
    like = models.BooleanField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    q_like = models.ForeignKey(Like, on_delete=models.CASCADE)


class AnswerLike(models.Model):
    like = models.BooleanField(default=0)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    a_like = models.ForeignKey(Like, on_delete=models.CASCADE)
