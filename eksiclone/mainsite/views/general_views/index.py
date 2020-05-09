from datetime import datetime
from django.views.generic import TemplateView

from mainsite.app_models import Title, Event
from mainsite.urls import mainsite_urls as url


@url.re_path(r'^$', name='index')
class IndexPage(TemplateView):
    template_name = 'mainsite/index/index.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'random_titles': ((title, title.random_entry) for title in Title.objects.random(5)),
            'events': Event.objects.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())
        }
