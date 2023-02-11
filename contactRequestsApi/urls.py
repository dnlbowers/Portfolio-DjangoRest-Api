from django.urls import path, include
from rest_framework import routers

from .views import ContactRequestViewSet

app_name = "contactRequestsApi"

router = routers.DefaultRouter()

router.register(r"contact-requests", ContactRequestViewSet, basename="contact-requests")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
        ))
]