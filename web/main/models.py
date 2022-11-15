from django.db import models
from django.db.models import Count


class MyUser(models.Model):
    password = models.CharField('Password', max_length=128)
    username = models.CharField('Username', max_length=150)
    email = models.CharField('Email', max_length=254)
    date_joined = models.DateTimeField('DateJoined')
    is_active = models.BooleanField('IsActive')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'


class Question(models.Model):
    title = models.CharField('Title', max_length=50)
    descr = models.TextField('Description')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author_fk = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class TagManager(models.Manager):
    def popular(self):
        return Tag.objects.annotate(
            occurrences=Count('questions')
        ).order_by('-occurrences')[:5]


class Tag(models.Model):
    tag = models.CharField('Tag', max_length=50)
    questions = models.ManyToManyField(Question)
    objects = TagManager()

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProfileManager(models.Manager):
    def best(self):
        best_members = list()
        for i in Profile.objects.order_by('-rating')[:5]:
            best_members.append(MyUser.objects.get(pk=i.user_fk_id).username)
        return best_members


class Profile(models.Model):
    avatar = models.CharField('Avatar', max_length=100, null=False)
    rating = models.IntegerField('Rating', default=0, null=False)
    user_fk = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    objects = ProfileManager()

    def __str__(self):
        return self.avatar

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Answer(models.Model):
    descr = models.TextField('Description')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    author_fk = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False)
    question_fk = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.descr

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
