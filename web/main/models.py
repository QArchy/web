from django.db import models


class Question(models.Model):
    title = models.CharField('Title', max_length=50)
    descr = models.TextField('Description')
    tags = models.CharField('Tags', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class QuestionTags(models.Model):
    tag = models.CharField('Tag', max_length=50)
    main_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
