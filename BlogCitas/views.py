from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .funciones import *
from django.contrib import messages
# Create your views here.

def principal(request):
    return render(request, 'BlogCitas/principal.html',{
        "promociones": Promociones.objects.all(), 
        "posts": Post.objects.order_by("-id")[:8]
    })

def blog(request):
    posts = Post.objects.order_by("-id")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'BlogCitas/blog.html', {
        'page_obj': page_obj
    })

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'BlogCitas/post.html',{
        "post": post
    })


def acerca_de(request):
    return render(request, 'BlogCitas/acerca_de.html')


def citas(request):
    return render(request, 'BlogCitas/citas.html',{
        "fechas": fechas()
    })


def nueva_cita(request):
    if request.method == 'POST':
        correo = request.POST["correo"]

        try:
            paciente = Paciente.objects.get(correo=correo)

        except Paciente.DoesNotExist:
            messages.add_message(request, messages.WARNING, 'El correo electrónico no esta registrado.')
            return HttpResponseRedirect(reverse("citas"))

        today = date.today()    
        if Citas.objects.filter(fecha__gt=today, paciente=paciente).count() >= 1:
            messages.add_message(request, messages.WARNING, 'Usted ya tiene una cita proximamente')
            return HttpResponseRedirect(reverse("principal"))
        
        fecha_cita = request.POST["feha_cita"]
        horario_cita = request.POST["horario_cita"]
        
        try:
            cita = Citas(paciente=paciente, fecha=fecha_cita, hora=horario_cita)
            cita.save()

        except:
            messages.add_message(request, messages.WARNING, 'No se pudo agendar la cita, intente más tarde.')
            return HttpResponseRedirect(reverse("citas"))

        messages.add_message(request, messages.SUCCESS, 'La cita se ha realizado con éxito')
        return HttpResponseRedirect(reverse("principal"))

    else:
        return HttpResponseRedirect(reverse("principal"))


def eliminar_cita(request):
    if request.method == "POST":      
        correo = request.POST["correo"]
    
        try:
            paciente = Paciente.objects.get(correo=correo)
        except Paciente.DoesNotExist:
            messages.add_message(request, messages.WARNING, "No tenemos registrado ese correo electrónico")
            return HttpResponseRedirect(reverse("eliminar_cita"))

        today = date.today() 
        try: 
            cita = Citas.objects.get(paciente=paciente, fecha__gt=today)
        except Citas.DoesNotExist:
            messages.add_message(request, messages.WARNING, "No hay ninguna cita que coincida")
            return HttpResponseRedirect(reverse("eliminar_cita"))

        accion = request.POST["accion"]
        if accion == "eliminar":
            cita.delete()
            messages.add_message(request, messages.SUCCESS, f"La cita de {cita.paciente.nombre} el día {cita.fecha} a las {cita.hora} se ha eliminado con éxito.")
            return HttpResponseRedirect(reverse("principal"))
        elif accion == "horario":
            horario = f"Tu cita es el día {cita.fecha} a las {cita.hora}"
            return render(request, 'BlogCitas/eliminar_cita.html',{
                "horario": horario
                })

    else:
        return render(request, 'BlogCitas/eliminar_cita.html')
