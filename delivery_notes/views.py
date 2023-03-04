from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DeliveryNote

def delivery_note_list(request):
    delivery_notes = DeliveryNote.get_all_delivery_notes()
    return render(request, 'delivery_notes/index.html', {'delivery_notes': delivery_notes})

def delivery_note_detail(request, delivery_note_id):
    delivery_note = DeliveryNote.objects.get(id=delivery_note_id)
    return render(request, 'delivery_notes/detail.html', {'delivery_note': delivery_note})

def delivery_note_create(request):
    if request.method == 'POST':
        delivery_note_number = request.POST['delivery_note_number']
        date = request.POST['date']
        invoice_number = request.POST['invoice_number']
        image = request.FILES['image']

        delivery_note = DeliveryNote(
            delivery_note_number=delivery_note_number,
            date=date,
            invoice_number=invoice_number,
            image=image
        )
        delivery_note.save()
        return redirect('delivery_notes:index')
    else:
        return render(request, 'delivery_notes/create.html')

def delivery_note_update(request, delivery_note_id):
    delivery_note = DeliveryNote.objects.get(id=delivery_note_id)

    if request.method == 'POST':
        delivery_note.delivery_note_number = request.POST['delivery_note_number']
        delivery_note.date = request.POST['date']
        delivery_note.invoice_number = request.POST['invoice_number']

        if request.FILES:
            delivery_note.image = request.FILES['image']

        delivery_note.save()
        return redirect('delivery_notes:index')
    else:
        return render(request, 'delivery_notes/update.html', {'delivery_note': delivery_note})

def delivery_note_delete(request, delivery_note_id):
    delivery_note = DeliveryNote.objects.get(id=delivery_note_id)
    delivery_note.delete()
    return redirect('delivery_notes:index')

def search_delivery_notes(request):
    if request.method == 'POST':
        query = request.POST['query']
        delivery_notes = DeliveryNote.search_delivery_note_by_number(query)
        return render(request, 'delivery_notes/index.html', {'delivery_notes': delivery_notes})
    else:
        return redirect('delivery_notes:index')
