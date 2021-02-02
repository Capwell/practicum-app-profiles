from django.views.generic.base import TemplateView

from .apps import NotesConfig


class HomeView(TemplateView):
    template_name = 'notes/home.html'

    def get_context_data(self, **kwargs):
        kwargs['app_name'] = NotesConfig.verbose_name
        return super(HomeView, self).get_context_data(**kwargs)
