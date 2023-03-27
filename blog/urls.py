from django.urls import path

from .views import HomeView, post_single, TagListView


app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:post_slug>/', post_single, name='post_single'),
    path('tag/<slug:tag>/', TagListView.as_view(), name='post_by_tag')
]
