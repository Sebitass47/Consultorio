from django.urls import path
from . import views

urlpatterns = [
     path("", views.principal, name="index"),
     path("blog", views.blog, name="blog"),
     path("post/<int:post_id>", views.post, name="post")
]