from factory import Faker
from factory.django import DjangoModelFactory

from . import models


class TemplateFactory(DjangoModelFactory):
    name = Faker("name")
    engine = Faker("word", ext_word_list=models.Template.ENGINE_CHOICES_LIST)
    template = None

    class Meta:
        model = models.Template
