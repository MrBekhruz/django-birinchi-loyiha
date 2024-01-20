from django.shortcuts import render,redirect,get_object_or_404
from .models import *  #model fayldan malumot olib keldik
from .forms import *


def home(request):
    post = Post.objects.all () #funksiya modelda birinchisi post bulgani uchun Post deb oldim abyektning hammasini olib keldik 
    bulim = BulimData.objects.all()
    context = {
        'post':post,
        'bulim':bulim
    } #context bir uzgaruvchi post haqiqatdan ham post teng ekanligini isbotladik
    return render(request, 'index.html',context) # va oxirida albatta context , bilan html fayldan sung yoziladi 


def bulimdata(request, pk):
    bulim = get_object_or_404(BulimData, pk=pk)
    return render(request,'bulim.html',{'bulim':bulim})


def formpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("model_ruyxati")
    else:
        forma = PostForm()
    return render(request,'form.html',{'forma':forma})

