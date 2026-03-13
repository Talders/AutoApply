from django.urls import path
from .views import pdf_dashboard

urlpatterns = [
    path('', pdf_dashboard, name='pdf_dashboard'),
]