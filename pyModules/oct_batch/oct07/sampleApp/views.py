# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
	a = int(request.GET['a'])
	b = int(request.GET['b'])
	return HttpResponse("Output is = %s"%(a+b))
