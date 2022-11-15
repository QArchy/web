from .models import *


class DataMixin:
    def get_template_context(self, **kwargs):
        context = kwargs
        context['best_members'] = Profile.objects.best()
        context['popular_tags'] = Tag.objects.popular()
        if 'question' in context:
            context['question'] = Question.objects.get(pk=context['question'])
        return context
