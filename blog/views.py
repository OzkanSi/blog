from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.http import HttpResponse
from django.template import loader

# Create your views here.



def index(request):
    context = dict()

    context['posts'] = Post.objects.all()
    context['cat'] = Category.objects.all()
    return render(request, 'index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)


def category_show(request, category_slug):
    context = dict()
    context['cat'] = Category.objects.all()
    context['category'] = get_object_or_404(
        Category, slug=category_slug,
    )

    context['items'] = Post.objects.filter(
        category=context['category'],
    )
    return render(request, 'category_show.html', context)