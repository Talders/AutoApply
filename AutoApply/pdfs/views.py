from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def pdf_dashboard(request):
    return render(request, "pdfs/pdf_dashboard.html")
