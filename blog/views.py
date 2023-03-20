from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    """
    Отобрпжение домашней страницы.
    """

    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    def get_template_names(self):
        """
        Добавление по 10 постов по мере прокрутке скрола вниз.
        """
        if self.request.htmx:
            return 'blog/components/post-list-element.html'
        return 'blog/index.html'
