from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag('blog/components/tags-cloud.html')
def sidebar_tag_cloud():
    """
    Реализует облако тегов.
    """
    tags = Tag.objects.all()
    return {'tags': tags}
