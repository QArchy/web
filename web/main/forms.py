from .models import Question
from django.forms import ModelForm, TextInput, Textarea


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title", "descr", "tags"]
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control text-white',
                    'style': 'background-color: rgb(255, 255, 255, 0.1)',
                    'placeholder': 'Input title'
                }
            ),
            'descr': Textarea(
                attrs={
                    'class': 'form-control text-white',
                    'style': 'background-color: rgb(255, 255, 255, 0.1)',
                    'placeholder': 'Input description'
                }
            ),
            'tags': TextInput(
                attrs={
                    'class': 'form-control text-white',
                    'style': 'background-color: rgb(255, 255, 255, 0.1)',
                    'placeholder': 'Input tags'
                }
            )
        }
