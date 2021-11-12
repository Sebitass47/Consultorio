from datetime import date, timedelta
from .models import *

def fechas():
    fechas = []

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    festivos = ["1-1", "1-2", "1-3", "1-4", "1-5", "1-6", "5-7", "12-24", "12-25", "12-26", "12-27", "12-28", "12-29", "12-30", "12-31", "11-9"]

    today = date.today()

    for i in range(1,15):

        new_date = today + timedelta(days=i)

        if dias[new_date.weekday()] == "Domingo" or dias[new_date.weekday()] == "Sabado":
            pass

        else:
            fecha_usuario = dias[new_date.weekday()] + " "+ str(new_date.day) + " de " + meses[new_date.month - 1] + " de " + str(new_date.year)
            fecha_sin_año = str(new_date.month) + "-" + str(new_date.day)

            if fecha_sin_año in festivos:
                pass
            else:
                new_date = str(new_date)
                fecha = {"fecha_numerica": new_date, "fecha_usuario": fecha_usuario}
                fechas.append(fecha)
            
    return fechas



def horario(fecha):
    horariosdisponibles = []

    horarios = HorariosTrabajo.objects.values_list("hora").exclude(hora__in = Citas.objects.values_list("hora").filter(fecha=fecha))

    for horario in horarios:

        horariosdisponibles.append(str(horario[0]))

    return horariosdisponibles