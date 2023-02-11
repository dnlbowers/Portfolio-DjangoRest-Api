from django.test import TestCase

# from .models import ContactRequest
from .factories import ContactRequestFactory

class ContactRequestModelTest(TestCase):

    def test_str(self):
        contact_request = ContactRequestFactory()
        self.assertEqual(str(contact_request), contact_request.name)