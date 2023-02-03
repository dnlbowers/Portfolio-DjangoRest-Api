from factory import DjangoModelFactory, Faker

from ..models import ContactRequest

class ContactRequestFactory(DjangoModelFactory):
    class Meta:
        model = ContactRequest

    name = Faker("name")
    email = Faker("email")
    reason = Faker("word")
    message = Faker("text")