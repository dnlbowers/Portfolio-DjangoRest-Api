from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/portfolio/", include("projectsApi.urls", namespace="projectsApi")),
    path("api/contact/", include("contactRequestsApi.urls", namespace="contactRequestsApi")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
