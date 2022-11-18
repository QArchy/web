from django.contrib import admin
from .models import Question, Tag, Profile, Answer

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Answer)

