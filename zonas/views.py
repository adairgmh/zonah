from django.shortcuts import render

from django.shortcuts import render
from .models import Estado
import pytz
from django.utils import timezone

def obtener_hora_estado(request, estado_id):
    estado = Estado.objects.get(pk=estado_id)
    zona_horaria = estado.zona_horaria
    
    usuario_timezone = pytz.timezone(zona_horaria)
    hora_actual = timezone.now().astimezone(usuario_timezone)
    
    context = {
        'estado': estado,
        'hora_actual': hora_actual,
    }
    return render(request, 'hora_estado.html', context)

