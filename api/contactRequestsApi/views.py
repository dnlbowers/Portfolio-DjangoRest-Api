from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import ContactRequest

from .serializers import ContactRequestSerializer


class ContactRequestViewSet(CreateModelMixin, GenericViewSet):

    serializer_class = ContactRequestSerializer

    queryset = ContactRequest.objects.all()   
