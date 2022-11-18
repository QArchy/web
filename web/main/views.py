import datetime

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from .utils import *
from .forms import *
from .models import *
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
        return Question.objects.annotate(
            likes=Count('questionlike')
        ).order_by('-likes')


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


# class Question_f(DataMixin, ListView):
#     paginate_by = 30
#     model = Answer
#     template_name = 'main/question.html'
#     context_object_name = 'answers'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         template_context = self.get_template_context(
#             question=self.kwargs['question_id'], title="Question"
#         )
#         return dict(list(context.items()) + list(template_context.items()))
#
#     def get_queryset(self):
#         try:
#             answers = Question.objects.get(pk=self.kwargs['question_id']).answer_set.all()
#         except:
#             raise Http404
#         else:
#             return answers


def Question_f(request, question_id):
    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': "Question"
    }

    try:
        answers = Question.objects.get(pk=question_id).answer_set.all()
    except:
        raise Http404
    else:
        paginator = Paginator(answers, 30)
        context['paginator'] = paginator
        context['question'] = Question.objects.get(pk=question_id)
        context['page_obj'] = paginator.get_page(request.GET.get('page'))

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)

        if answer_form.is_valid():
            answer = Answer(
                descr=answer_form.cleaned_data['descr'],
                correct=False,
                author_fk=Question.objects.get(pk=question_id).author_fk,
                question_fk=Question.objects.get(pk=question_id),
                #  date=datetime.datetime.now(),
            )
            answer.save()
            if len(paginator.page_range) > 1:
                if (len(answers) - 1) % 30 == 0:
                    print('REDIRECT + 1')
                    paginator = Paginator(answers, 30)
                    context['paginator'] = paginator
                    context['page_obj'] = paginator.get_page(str((int(request.GET.get('page')) + 1)))
                    return redirect('/question/%d?page=%d' % (question_id, len(paginator.page_range) + 1))
                else:
                    return redirect('/question/%d?page=%d' % (question_id, len(paginator.page_range)))
            else:
                return redirect('/question/%d' % question_id)
    else:
        context['answer_form'] = AnswerForm()

    return render(request, 'main/question.html', context)


def login(request):
    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': "Login"
    }
    return render(request, 'main/log_in.html', context)


def register(request):
    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': 'Registration'
    }

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            if profile_form.cleaned_data.get('avatar') is None:
                profile = Profile.objects.create(
                    user_fk=user,
                    avatar='web/main/static/img/default_avatar.svg',
                )
                profile.save()
            else:
                profile = Profile.objects.create(
                    user_fk=user,
                    avatar=profile_form.cleaned_data.get('avatar'),
                )
                profile.save()

            return redirect('login')
        else:
            context['form'] = form
            context['profile_form'] = profile_form
    else:
        context['form'] = RegisterUserForm()
        context['profile_form'] = ProfileForm()

    return render(request, 'main/register.html', context)


def settings(request):
    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': 'Settings'
    }

    if request.method == 'POST':
        form = SettingsUserForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data['first_name'])
            if request.user.username != form.cleaned_data['username'] and len(form.cleaned_data['username']) > 0:
                request.user.username = form.cleaned_data['username']
            if request.user.email != form.cleaned_data['email'] and len(form.cleaned_data['email']) > 0:
                request.user.email = form.cleaned_data['email']
            if request.user.first_name != form.cleaned_data['first_name'] and len(form.cleaned_data['first_name']) > 0:
                request.user.first_name = form.cleaned_data['first_name']
            request.user.save()
            if request.user.profile.avatar != form.cleaned_data['avatar'] and form.cleaned_data['avatar'] is not None:
                request.user.profile.avatar = form.cleaned_data['avatar']
            request.user.profile.save()
            return redirect('settings')
        else:
            context['form'] = form
    else:
        context['form'] = SettingsUserForm(initial={
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'avatar': request.user.profile.avatar,
        })

    return render(request, 'main/settings.html', context)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/log_in.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        template_context = self.get_template_context(title="Login")
        return dict(list(context.items()) + list(template_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def ask(request):
    def split_str(my_str):
        my_str = re.split(",| ", my_str)
        my_str = list(filter(None, my_str))
        my_str = list(dict.fromkeys(my_str))
        return my_str

    context = {
        'best_members': Profile.objects.best(),
        'popular_tags': Tag.objects.popular(),
        'title': 'Ask'
    }

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        tag_form = QuestionTagsForm(request.POST)

        if question_form.is_valid() and tag_form.is_valid():
            question = question_form.save(commit=False)
            question.author_fk = request.user
            #  question.date = datetime.datetime.now()
            question.save()

            tags_str = tag_form.cleaned_data['tag']
            tags_list = split_str(tags_str)
            for tag_str in tags_list:
                tag = Tag(
                    tag=tag_str
                )
                tag.save()
                tag.questions.add(question)
                tag.save()

            return redirect('question/%d' % question.pk)
        else:
            context['question_form'] = question_form
            context['tag_form'] = tag_form
    else:
        context['question_form'] = QuestionForm()
        context['tag_form'] = QuestionTagsForm()

    return render(request, 'main/ask.html', context)
