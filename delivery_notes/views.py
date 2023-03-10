from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

from .models import DeliveryNote
from .forms import DeliveryNoteForm


class DeliveryNoteListView(View):
    def get(self, request):
        delivery_notes = DeliveryNote.objects.all()
        return render(request, 'delivery_notes/base.html', {'delivery_notes': delivery_notes})


class DeliveryNoteDetailView(View):
    def get(self, request, pk):
        delivery_note = get_object_or_404(DeliveryNote, pk=pk)
        return render(request, 'delivery_notes/detail.html', {'delivery_note': delivery_note})


class DeliveryNoteCreateView(View):
    def get(self, request):
        form = DeliveryNoteForm()
        return render(request, 'delivery_notes/delivery_note_create.html', {'form': form})

    def post(self, request):
        form = DeliveryNoteForm(request.POST)
        if form.is_valid():
            delivery_note = form.save()
            messages.success(request, 'Delivery note created successfully.')
            return redirect('delivery_notes:list')
        return render(request, 'delivery_notes/delivery_note_create.html', {'form': form})


class DeliveryNoteUpdateView(View):
    def get(self, request, pk):
        delivery_note = get_object_or_404(DeliveryNote, pk=pk)
        form = DeliveryNoteForm(instance=delivery_note)
        return render(request, 'delivery_notes/update.html', {'form': form})

    def post(self, request, pk):
        delivery_note = get_object_or_404(DeliveryNote, pk=pk)
        form = DeliveryNoteForm(request.POST, instance=delivery_note)
        if form.is_valid():
            delivery_note = form.save()
            messages.success(request, 'Delivery note updated successfully.')
            return redirect('delivery_notes:list')
        return render(request, 'delivery_notes/update.html', {'form': form})


class DeliveryNoteDeleteView(View):
    def get(self, request, pk):
        delivery_note = get_object_or_404(DeliveryNote, pk=pk)
        return render(request, 'delivery_notes/delete.html', {'delivery_note': delivery_note})

    def post(self, request, pk):
        delivery_note = get_object_or_404(DeliveryNote, pk=pk)
        delivery_note.delete()
        messages.success(request, 'Delivery note deleted successfully.')
        return redirect('delivery_notes:list')
