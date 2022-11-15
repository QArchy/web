from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .Mixin import *
from .forms import QuestionForm
from .forms import QuestionTagsForm
from .models import Question, Answer, Profile
from .models import Tag
import re


class Questions_new(DataMixin, ListView):
    paginate_by = 20
    model = Question
    template_name = 'main/questions.html'
    context_object_name = 'questions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        template_context = self.get_template_context(title="New Questions")
        return dict(list(context.items()) + list(template_context.items()))

    def get_queryset(self):
        return Question.objects.all().order_by('-date')


class Questions_hot(DataMixin, ListView):
    paginate_by = 20
    model = Question
    template_name = 'main/questions.html'
    context_object_name = 'questions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        template_context = self.get_template_context(title="Hot Questions")
        return dict(list(context.items()) + list(template_context.items()))

    def get_queryset(self):
        return Question.objects.all().order_by('-likes')


class Questions_tag(DataMixin, ListView):
    paginate_by = 20
    model = Question
    template_name = 'main/questions.html'
    context_object_name = 'questions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        template_context = self.get_template_context(
            question_by_tag=self.kwargs['tag'], title="Questions By Tag"
        )
        return dict(list(context.items()) + list(template_context.items()))

    def get_queryset(self):
        try:
            questions = Tag.objects.get(tag=self.kwargs['tag']).questions.all()
        except:
            raise Http404
        else:
            return questions


class Question_f(DataMixin, ListView):
    paginate_by = 30
    model = Answer
    template_name = 'main/question.html'
    context_object_name = 'answers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        template_context = self.get_template_context(
            question=self.kwargs['question_id'], title="Question"
        )
        return dict(list(context.items()) + list(template_context.items()))

    def get_queryset(self):
        try:
            answers = Question.objects.get(pk=self.kwargs['question_id']).answer_set.all()
        except:
            raise Http404
        else:
            return answers


def login(request):
    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': "Login"
    }
    return render(request, 'main/log_in.html', context)



class User(DataMixin, ListView):
    paginate_by = 20
    model = Question
    template_name = 'main/logged_in.html'
    context_object_name = 'questions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        template_context = self.get_template_context(title="User")
        return dict(list(context.items()) + list(template_context.items()))

    def get_queryset(self):
        return Question.objects.all().order_by('-date')


def register(request):
    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': "Register"
    }
    return render(request, 'main/register.html', context)


def settings(request):
    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': "Settings"
    }
    return render(request, 'main/settings.html', context)


def split_str(my_str):
    my_str = my_str.lower()
    my_str = re.split(",| ", my_str)
    my_str = list(filter(None, my_str))
    return my_str


def check_word_len(words):
    for word in words:
        if len(word) > 12:
            return False
    return True


def create(request):
    error = ''
    if request.method == 'POST':
        formQuestion = QuestionForm(request.POST)
        formTags = QuestionTagsForm(request.POST)
        if formQuestion.is_valid() and formTags.is_valid():
            if check_word_len(split_str(formQuestion.cleaned_data['title'])):
                if check_word_len(split_str(formQuestion.cleaned_data['descr'])):
                    if check_word_len(split_str(formTags.cleaned_data['tag'])):
                        formQuestion.save()
                        for el in split_str(formTags.cleaned_data['tag']):
                            tag = Tag(tag=el, question_fk_id=Question.objects.latest('id').pk)
                            tag.save()
                        return redirect('home')
                    else:
                        error = 'Warning: Too long word in tags'
                else:
                    error = 'Warning: Too long word in description'
            else:
                error = 'Warning: Too long word in title'
        else:
            error = 'Warning: Form was incorrect'

    formQuestion = QuestionForm()
    formTags = QuestionTagsForm()
    context = {
        'formQuestion': formQuestion,
        'formTags': formTags,
        'error': error,
        'title': "Ask"
    }
    return render(request, 'main/ask.html', context)
