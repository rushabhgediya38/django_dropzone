from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import post

from .forms import post_form


# Create your views here.


def home(request):
    return HttpResponse('home page')


def post_create(request):
    if request.method == 'POST':

        name1 = request.POST['name']
        username1 = request.POST['username']
        files = [request.FILES.get('file[%d]' % i) for i in range(0, len(request.FILES))]
        images = request.FILES.get('file[0]', None)

        print(name1, username1)
        for f in files:
            data = f
            posttt = post.objects.create(name=name1, username=username1, img=data)
            posttt.save()
        # filess = request.FILES.getlist('images')
        return redirect('/')

    else:
        return render(request, 'post_create.html', {
        })
