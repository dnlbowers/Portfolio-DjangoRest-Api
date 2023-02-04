from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/projects', views.ProjectViewSet, basename='projects')
router.register(r'api/upcomingprojects', views.UpcomingProjectViewSet, basename='upcomingprojects')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
        ))
]
