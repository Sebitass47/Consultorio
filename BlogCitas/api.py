from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .funciones import horario
from .models import *
import json

from .models import *

def registro(request):
    if request.method == 'POST':
        content = json.loads(request.body)
        if content is not None:
            try:
                paciente = Paciente(nombre = content['nombre'], correo = content['correo'], fecha_nacimiento = content['fecha_nacimiento'], genero = content['genero'])
                paciente.save()
                return JsonResponse({"success": "Usuario registrado"}, status=201)
            except:
                return JsonResponse({"error": "Correo electrónico ya registrado en otra cuenta"}, status=400)
        else:
            return JsonResponse({"error": "Porfavor llena todo el formulario"}, status=400)
    else:
        return HttpResponseRedirect(reverse("principal"))


def horarios(request, fecha):


        try:
            print(1)
            print(horario(fecha))
            return JsonResponse({"horarios": horario(fecha)}, status=200)
            
        except:
            print(3)
            return JsonResponse({"error": "Algo salió mal, intente más tarede"}, status=400)
    
    