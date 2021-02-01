from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import post, post123

from .forms import post_form, post_py, post123_form


# Create your views here.


def home(request):
    return HttpResponse('home page')


def post_create(request):
    if request.method == 'POST' or request.FILES:

        name1 = request.POST.get('name')
        username1 = request.POST.get('username')

        files = [request.FILES.get('file[%d]' % i) for i in range(0, len(request.FILES))]
        images = request.FILES.get('file[0]', None)

        if files:
            for f in files:
                data = f
                posttt = post.objects.create(name=name1, username=username1, img=data)
                posttt.save()
            # filess = request.FILES.getlist('images')
            return redirect('/')
        else:
            posttt = post.objects.create(name=name1, username=username1)
            posttt.save()
            return redirect('/')

    else:
        return render(request, 'post_create.html', {
        })


def create(request):
    form = post_py(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)

    context = {'form': form}
    return render(request, 'post.html', context)


def final_post(request):
    if request.method == 'POST' or request.FILES:
        name11 = request.POST.get('name')
        username11 = request.POST.get('username')
        img12 = request.FILES.get('img1')

        files = [request.FILES.get('file[%d]' % i) for i in range(0, len(request.FILES))]
        images = request.FILES.get('file[0]', None)

        for f in files:
            data = f
            posttt = post123.objects.create(name=name11, username=username11, img=data, img1=img12)
            posttt.save()
            return redirect('/')

        if img12:
            posttt = post123.objects.create(name=name11, username=username11, img1=img12)
            posttt.save()
            return redirect('/')

        if files:
            for f in files:
                data = f
                posttt = post123.objects.create(name=name11, username=username11, img=data)
                posttt.save()
                return redirect('/')

    return render(request, 'final_post.html')
