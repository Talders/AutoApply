from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class CustomUser(AbstractUser):
    smtp_host = models.CharField(max_length=255, blank=True, null=True)
    smtp_port = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(65535)]
    )
    smtp_username = models.CharField(max_length=255, blank=True, null=True)
    smtp_password = models.CharField(max_length=255, blank=True, null=True)
    smtp_use_tls = models.BooleanField(default=True)

    imap_host = models.CharField(max_length=255, blank=True, null=True)
    imap_port = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(65535)]
    )
    imap_username = models.CharField(max_length=255, blank=True, null=True)
    imap_password = models.CharField(max_length=255, blank=True, null=True)
    imap_use_ssl = models.BooleanField(default=True)