from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'smtp_host', 'smtp_port', 'smtp_username', 'smtp_password', 'smtp_use_tls',
            'imap_host', 'imap_port', 'imap_username', 'imap_password', 'imap_use_ssl',
        )