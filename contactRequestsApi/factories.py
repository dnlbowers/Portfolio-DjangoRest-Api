from factory import Faker, django
from .models import ContactRequest

class ContactRequestFactory(django.DjangoModelFactory):
    class Meta:
        model = ContactRequest

    name = Faker("name")
    email = Faker("email")
    reason = Faker("word")
    message = Faker("text")