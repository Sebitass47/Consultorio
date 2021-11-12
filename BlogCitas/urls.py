from django.urls import path
from . import views
from . import api

urlpatterns = [
     path("", views.principal, name="principal"),
     path("blog", views.blog, name="blog"),
     path("post/<int:post_id>", views.post, name="post"),
     path("acerca_de", views.acerca_de, name="acerca_de"),
     path("citas", views.citas, name="citas"),
     path("registro", api.registro, name="registro"),
     path("horarios/<fecha>", api.horarios, name="horarios"),
     path("nueva_cita", views.nueva_cita, name="nueva_cita"),
     path("eliminar_cita",views.eliminar_cita, name="eliminar_cita")
]