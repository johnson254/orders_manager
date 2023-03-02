from django.shortcuts import render

def index(request):
    return render(request, 'delivery_notes/index.html')
