from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/portfolio/", include("projectsApi.urls", namespace="projectsApi")),
    path("api/contact/", include("contactRequestsApi.urls", namespace="contactRequestsApi")),
]
