from django.views.generic import TemplateView, ListView

from learn.models import Expression


class Index(TemplateView):
    template_name = 'learn/index.html'


class ExpressionListView(ListView):
    model = Expression
    template_name = 'learn/try.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(ExpressionListView, self).get_queryset()
        qs = qs.order_by("?")
        return qs

