from django.shortcuts import render


def home(request):
    return render(request, 'mama_fua/dashboard.html')


def index(request):
    return render(request, 'mama_fua/index.html')


def cloth_details(request):
    return render(request, 'mama_fua/cloth_details.html')


def cart(request):
    return render(request, 'mama_fua/cart.html')


def checkout(request):
    return render(request, 'mama_fua/checkout.html')


def confirm_order(request):
    return render(request, 'mama_fua/confirm_order.html')


def history(request):
    return render(request, 'mama_fua/history.html')


def create_order(request):
    return render(request, 'mama_fua/create_order.html')
