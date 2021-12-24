from typing import get_args
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
class Home(TemplateView):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')
    