from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delivery_notes/', include('delivery_notes.urls', namespace='delivery_notes')),
]
