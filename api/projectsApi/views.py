
from rest_framework import viewsets

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(status=1).order_by("completion_date")
    serializer_class = ProjectSerializer


class UpcomingProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(status=2).order_by("completion_date")
    serializer_class = ProjectSerializer
