from django.urls import path

from .views import (
    DeliveryNoteListView,
    DeliveryNoteDetailView,
    DeliveryNoteCreateView,
    DeliveryNoteUpdateView,
    DeliveryNoteDeleteView,
)

app_name = 'delivery_notes'

urlpatterns = [
    path('', DeliveryNoteListView.as_view(), name='delivery_note_list'),
    path('<int:pk>/', DeliveryNoteDetailView.as_view(), name='delivery_note_detail'),
    path('create/', DeliveryNoteCreateView.as_view(), name='delivery_note_create'),
    path('<int:pk>/update/', DeliveryNoteUpdateView.as_view(), name='delivery_note_update'),
    path('<int:pk>/delete/', DeliveryNoteDeleteView.as_view(), name='delivery_note_delete'),
]
