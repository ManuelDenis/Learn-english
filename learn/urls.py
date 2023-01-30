from django.urls import path
from learn import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]