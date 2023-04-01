import factory

from django.contrib.auth.models import User
from factory.faker import faker

from .models import Post

FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    """
    Генератор постов для заполнения контента.
    """
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=12)
    subtitle = factory.Faker('sentence', nb_words=12)
    slug = factory.Faker('slug')
    author = User.objects.get_or_create(username='admin')[0]
    status = 'published'

    @factory.lazy_attribute
    def content(self):
        x = ''
        for _ in range(0, 5):
            x += '\n' + FAKE.paragraph(nb_sentences=30) + '\n'
        return x

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(extracted)
        else:
            self.tags.add(
                'python',
                'osint',
                'django',
                'home',
                'back-end'
            )
