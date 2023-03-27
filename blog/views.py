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
    related = Post.objects.filter(author=post.author)[:5]
    return render(request,
                  'blog/single_post.html',
                  {
                      'post': post,
                      'related': related
                  })


class TagListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs["tag"]])

    def get_template_names(self):
        return 'blog/tags.html'
