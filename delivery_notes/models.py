from django.db import models

class DeliveryNote(models.Model):
    delivery_note_number = models.CharField(max_length=255)
    date = models.DateField()
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
