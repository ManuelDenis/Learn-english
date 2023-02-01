from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
import openai
from learn.forms import MessageForm
from learn.models import Expression


class Index(View):
    form_class = MessageForm
    template_name = 'learn/index.html'

    def get(self, request, *args, **kwargs):
        form = MessageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = MessageForm(self.request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if self.request.user is not None:
                if self.request.user.is_authenticated:
                    obj.user = self.request.user
            obj.save()
            messages.success(request, "Mesajul a fost trimis! Iti multumim!")
            return redirect('/')
        return render(request, self.template_name, {'form': form})


class ExpressionListView(ListView):
    model = Expression
    template_name = 'learn/try.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(ExpressionListView, self).get_queryset()
        qs = qs.order_by("?")
        return qs





