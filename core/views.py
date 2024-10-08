from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


@login_required
def customer_page(request):
    return render(request, "home.html")


@login_required
def bearer_page(request):
    return render(request, "home.html")
