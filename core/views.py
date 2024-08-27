from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def customer_page(request):
    return render(request, "home.html")


def bearer_page(request):
    return render(request, "home.html")
