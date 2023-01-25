from django.shortcuts import render
from django.views.generic.base import View

from .models import Picture, Category,Video
from django.urls import reverse_lazy

# Create your views here.


def PictureList(request):
    category = request.GET.get('category')
    if category is None:
        photos = Picture.objects.all()
    else:
        photos = Picture.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, template_name='base.html',context=context)


def PictureDetail(request, pk):
    photo = Picture.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, template_name='picture_detail.html',context=context)


def VideoList(request):
    category = request.GET.get('category')
    if category is None:
        videos = Video.objects.all()
    else:
        videos = Video.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'videos': videos}
    return render(request, template_name='videos.html',context=context)


def VideoDetail(request, pk):
    video = Video.objects.get(id=pk)
    context = {'video': video}
    return render(request, template_name='video_detail.html',context=context)


