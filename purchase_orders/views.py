from django.shortcuts import render

def index(request):
    return render(request, 'purchase_orders/index.html')
