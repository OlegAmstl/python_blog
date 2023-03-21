from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

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


def post_single(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status='published')
    return render(request, 'blog/single_post.html', {'post': post})
