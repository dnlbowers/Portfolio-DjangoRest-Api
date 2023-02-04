from django.urls import path, include
from rest_framework import routers

from .views import ContactRequestViewSet

router = routers.DefaultRouter()

router.register(r"api/contact-requests", ContactRequestViewSet, basename="contact-requests")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
        ))
]