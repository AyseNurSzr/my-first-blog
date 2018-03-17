from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render, redirect


def base(request):
	return render(request,'blog/base.html',locals())
