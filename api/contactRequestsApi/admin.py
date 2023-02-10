from django.contrib import admin
from .models import ContactRequest

# Register your models here.
@admin.register(ContactRequest)
class contactRequestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reason', 'created_at')