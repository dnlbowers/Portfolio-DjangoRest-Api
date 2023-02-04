from django.test import TestCase

from .factories import ContactRequestFactory
from .serializers import ContactRequestSerializer

class ContactRequestSerializerTestCase(TestCase):
    def test_serializer(self):
        contact_request = ContactRequestFactory()
        serializer = ContactRequestSerializer(contact_request)
        self.assertEqual(serializer.data, {
            "id": contact_request.id,
            "name": contact_request.name,
            "email": contact_request.email,
            "reason": contact_request.reason,
            "message": contact_request.message,
            
        })