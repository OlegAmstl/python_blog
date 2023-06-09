from django.urls import path

from .views import HomeView, PostSearchView, TagListView, post_single
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('<slug:post_slug>/', post_single, name='post_single'),
    path('tag/<slug:tag>/', TagListView.as_view(), name='post_by_tag'),

]
