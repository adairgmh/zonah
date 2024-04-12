from django.urls import path, include
from . import views

urlpatterns = [
    path('hora/<int:estado_id>/', views.obtener_hora_estado, name='hora_estado'),
]