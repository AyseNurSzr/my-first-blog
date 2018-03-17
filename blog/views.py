from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

def base(request):
    return render(request, 'blog/base.html',locals())