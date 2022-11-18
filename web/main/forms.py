from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
from django.forms import ModelForm, TextInput, Textarea, FileInput, EmailField


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title", "descr"]
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'title',
                    'id': 'title',
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Input title',
                    'minlength': '4',
                }
            ),
            'descr': Textarea(
                attrs={
                    'name': 'description',
                    'id': 'description',
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Input description',
                    'minlength': '10',
                    'style': 'resize:none;',
                }
            ),
        }


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('descr', )
        widgets = {
            'descr': Textarea(
                attrs={
                    'name': 'description',
                    'id': 'description',
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Input answer',
                    'minlength': '10',
                    'style': 'resize:none;',
                    'rows': '3',
                }
            ),
        }


class QuestionTagsForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']
        widgets = {
            'tag': TextInput(
                attrs={
                    'name': 'title',
                    'id': 'title',
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Input tag(s)',
                }
            ),
        }


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login'
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Input login',
            'minlength': '4',
            'maxlength': '20',
        })
        self.fields['email'].label = 'Email'
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Input email',
            'minlength': '4',
            'maxlength': '20',
        })
        self.fields['first_name'].label = 'Nickname'
        self.fields['first_name'].widget.attrs.update({
            'required': '',
            'name': 'first_name',
            'id': 'first_name',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Input nickname',
            'minlength': '4',
            'maxlength': '20',
        })
        self.fields['password1'].label = 'Password'
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Input password',
            'minlength': '8',
            'maxlength': '20',
        })
        self.fields['password2'].label = 'Repeat password'
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Repeat password',
            'minlength': '8',
            'maxlength': '20',
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')


class ProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].required = False

    class Meta:
        model = Profile
        fields = ('avatar',)
        widgets = {
            'avatar': FileInput(
                attrs={
                    'name': 'avatar',
                    'id': 'avatar',
                    'type': 'file',
                    'class': 'text-white',
                }
            ),
        }


class SettingsUserForm(ModelForm):
    class Meta:
        model = SettingsModel
        fields = ('username', 'email', 'first_name', 'avatar')
        widgets = {
            'username': TextInput(
                attrs={
                    'name': 'username',
                    'id': 'username',
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Input login',
                }
            ),
            'email': TextInput(
                attrs={
                    'name': 'email',
                    'id': 'email',
                    'type': 'email',
                    'class': 'form-control',
                    'placeholder': 'Input email',
                }
            ),
            'first_name': TextInput(
                attrs={
                    'name': 'first_name',
                    'id': 'first_name',
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Input nickname',
                }
            ),
            'avatar': FileInput(
                attrs={
                    'name': 'avatar',
                    'id': 'avatar',
                    'type': 'file',
                    'class': 'text-white',
                }
            ),
        }


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login'
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Input login',
            'minlength': '4',
            'maxlength': '20',
        })
        self.fields['password'].label = 'Password'
        self.fields['password'].widget.attrs.update({
            'required': '',
            'name': 'password',
            'id': 'password',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Input password',
            'minlength': '8',
            'maxlength': '20',
        })

    class Meta:
        model = User
        fields = ('username', 'password')

