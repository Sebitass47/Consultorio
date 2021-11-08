from django.urls import path
from . import views

urlpatterns = [
     path("", views.principal, name="principal"),
     path("blog", views.blog, name="blog"),
     path("post/<int:post_id>", views.post, name="post"),
     path("acerca_de", views.acerca_de, name="acerca_de"),
     path("citas", views.citas, name="citas")
]