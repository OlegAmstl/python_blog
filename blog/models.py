from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager


class Post(models.Model):
    """
    Модель статьи.
    """

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок поста')
    subtitle = models.CharField(
        max_length=100,
        verbose_name='Подзаголовок поста')
    slug = models.SlugField(
        max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='post_author',
        verbose_name='Автор поста')
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Дата создания поста')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления поста')
    status = models.CharField(
        max_length=10, choices=options, default='draft')

    tags = TaggableManager()
    cover = models.ImageField(
        verbose_name="Обложка",
        help_text='Добавьте обложку',
        upload_to="covers/",
        blank=True
    )

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
