from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .forms import PostSearchForm
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
    """
    Отображение поста.
    """
    post = get_object_or_404(Post, slug=post_slug, status='published')
    related = Post.objects.filter(author=post.author)[:5]
    return render(request,
                  'blog/single_post.html',
                  {
                      'post': post,
                      'related': related
                  })


class TagListView(ListView):
    """
    Отображение постов по тегу.
    """
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs["tag"]])

    def get_template_names(self):
        if self.request.htmx:
            return 'blog/components/post-list-element-tag.html'
        return 'blog/tags.html'

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context


class PostSearchView(ListView):
    """
    Отображение постов из результата поиска.
    """
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    form_class = PostSearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Post.objects.filter(title__icontains=form.cleaned_data['q'])
        return []

    def get_template_names(self):
        if self.request.htmx:
            return 'blog/components/post-list-element-search.html'
        return 'blog/search.html'
