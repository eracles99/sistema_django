from typing import get_args
from django.shortcuts import render
from django.views.generic import TemplateView
class Home(TemplateView):
    def get(self,request,*args, **kwargs):
        return render(request,'index.html')
    