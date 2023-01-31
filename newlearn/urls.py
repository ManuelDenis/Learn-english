from django.urls import path
from newlearn import views

urlpatterns = [
    path('', views.openai_view, name='newlearn')
]