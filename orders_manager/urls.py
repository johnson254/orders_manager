from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delivery_notes/', include('delivery_notes.urls')),
    path('invoices/', include('invoices.urls')),
    path('purchase_orders/', include('purchase_orders.urls')),
    path('users/', include('users.urls')),
]
