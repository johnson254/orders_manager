from django.urls import path

from . import views

app_name = 'delivery_notes'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:delivery_note_id>/', views.detail, name='detail'),
    # add more paths as needed
]
