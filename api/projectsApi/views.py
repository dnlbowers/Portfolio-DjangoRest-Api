
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.


class ProjectViewSet(GenericViewSet, ListModelMixin):
    queryset = Project.objects.filter(status=1).order_by("completion_date")
    serializer_class = ProjectSerializer


class UpcomingProjectViewSet(GenericViewSet, ListModelMixin):
    queryset = Project.objects.filter(status=2).order_by("completion_date")
    serializer_class = ProjectSerializer
