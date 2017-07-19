from django.shortcuts import render

# Create your views here.

# Temp
from django.http import HttpResponse
from django.contrib.auth.views import login_required
from django.views import View
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'website/index.html'
