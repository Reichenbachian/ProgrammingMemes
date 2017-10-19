from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.views import login as loginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
import os
from random import random
import base64

# Create your views here.
def Landing(request):
	path = '../Memes/'
	images = os.listdir(path)
	image = images[int(random()*len(images))]
	b64_image = base64.b64encode(open(path+image, 'rb').read())
	return render(request, 'MemeServer/HomePage.html', {'Image': b64_image})
