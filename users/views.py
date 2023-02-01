from django.shortcuts import render
from django.views.generic import CreateView
from users.models import Message


class MessageCreateView(CreateView):
    model = Message
    template_name = 'learn/index.html'
    fields = ['name', 'email', 'message']
