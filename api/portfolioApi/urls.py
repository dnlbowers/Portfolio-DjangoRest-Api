from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("projectsApi.urls")),
    path("", include("contactRequestsApi.urls")),
]
