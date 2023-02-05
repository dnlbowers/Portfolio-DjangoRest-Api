from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'projectsApi'

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'upcomingprojects', views.UpcomingProjectViewSet, basename='upcomingprojects')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
        ))
]
