import os
from django.template.defaultfilters import register
from .models import *


class DataMixin:
    def get_template_context(self, **kwargs):
        context = kwargs
        context['best_members'] = Profile.objects.best()
        context['popular_tags'] = Tag.objects.popular()
        return context


@register.filter
def filename(file):
    return os.path.basename(file)

