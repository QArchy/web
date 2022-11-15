from .models import Question
from .models import Tag
from django.forms import ModelForm, TextInput, Textarea


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title", "descr"]
        widgets = {
            'title': TextInput(
                attrs={
                    'id': 'inputTitle',
                    'class': 'form-control',
                    'placeholder': 'Input title',
                    'minlength': 10,
                }
            ),
            'descr': Textarea(
                attrs={
                    'id': 'inputDescription',
                    'class': 'form-control',
                    'placeholder': 'Input description',
                    'minlength': 20,
                    'style': 'resize:none;'
                }
            ),
        }


class QuestionTagsForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["tag"]
        widgets = {
            'tag': TextInput(
                attrs={
                    'id': 'inputTags',
                    'class': 'form-control',
                    'placeholder': 'Input tags',
                }
            ),
        }