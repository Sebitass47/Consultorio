from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.

def principal(request):
    return render(request, 'BlogCitas/principal.html',{
        "promociones": Promociones.objects.all(), 
        "posts": Post.objects.order_by("-id")[:6]
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
    return render(request, 'BlogCitas/citas.html')
