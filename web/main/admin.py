from django.contrib import admin
from .models import Question, Tag, Profile, Answer, MyUser

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Answer)
admin.site.register(MyUser)

