from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    """
    Отобрпжение домашней страницы.
    """

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
