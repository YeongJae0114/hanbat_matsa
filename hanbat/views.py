from django.shortcuts import render, redirect, get_object_or_404
from .forms import pythform
from .models import pyth

def index(request):
    return render(request,'likelion.html')

def joinus(request):
    return render(request,'joinus.html')

def modelformcreate(request):
    if request.method =='POST':
        form = pythform(request.POST)
        if form.is_valid(): #데이터 유효성 검사
            form.save()
            return redirect('index')
    else:
        form = pythform()
    return render(request, 'form_create1.html', {'form':form})

def submit(request):
    posts = pyth.objects.all()
    return render(request,'submit.html',{'posts':posts})


def detail(request, pyth_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    pyth_detail = get_object_or_404(pyth, pk=pyth_id)
    # blog_id 번째 블로그 글을 detail.html로 띄우주는 코드

    return render(request, 'detail.html', {'pyth_detail':pyth_detail })

def delete(request, pyth_id):
    post = pyth.objects.get(id=pyth_id)
    post.delete()
    return redirect(request,'submit')
