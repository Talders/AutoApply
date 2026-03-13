from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Mail Einstellungen", {'fields': (
            'smtp_host', 'smtp_port', 'smtp_username', 'smtp_password', 'smtp_use_tls',
            'imap_host', 'imap_port', 'imap_username', 'imap_password', 'imap_use_ssl',
        )}),
    )

# Register your models here.
