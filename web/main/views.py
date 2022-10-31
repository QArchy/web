from django.shortcuts import render, redirect

from .forms import QuestionForm
from .models import Question
from .models import QuestionTags
import re


def questions(request):
    _questions = Question.objects.all().order_by('-id')
    return render(request, 'main/questions.html', {'title': 'Main page',
                                                   'questions': _questions})


def question(request, question_id: int):
    _question = Question.objects.get(pk=question_id)
    return render(request, 'main/question.html', {'title': 'Question',
                                                  'question': _question})


def about(request):
    return render(request, 'main/about.html')


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
        form = QuestionForm(request.POST)
        if form.is_valid():
            if check_word_len(split_str(form.cleaned_data['title'])):
                if check_word_len(split_str(form.cleaned_data['descr'])):
                    if check_word_len(split_str(form.cleaned_data['tags'])):
                        form.save()
                        for el in split_str(form.cleaned_data['tags']):
                            tags = QuestionTags(tag=el, main_question_id=Question.objects.latest('id').pk)
                            tags.save()
                        return redirect('home')
                    else:
                        error = 'Warning: Too long word in tags'
                else:
                    error = 'Warning: Too long word in description'
            else:
                error = 'Warning: Too long word in title'
        else:
            error = 'Warning: Form was incorrect'

    form = QuestionForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
