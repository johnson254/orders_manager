from django import forms
from .models import DeliveryNote


class DeliveryNoteForm(forms.ModelForm):
    class Meta:
        model = DeliveryNote
        fields = ['delivery_note_number', 'date', 'invoice_number', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
