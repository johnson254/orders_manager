from django.db import models

class DeliveryNote(models.Model):
    delivery_note_number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    invoice_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='delivery_notes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.delivery_note_number

    def save(self, *args, **kwargs):
        super(DeliveryNote, self).save(*args, **kwargs)

    @staticmethod
    def get_all_delivery_notes():
        return DeliveryNote.objects.all()

    @staticmethod
    def search_delivery_note_by_number(delivery_note_number):
        return DeliveryNote.objects.filter(delivery_note_number__icontains=delivery_note_number)
