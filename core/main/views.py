from re import L
from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import Category,Shoose,Brend
# Create your views here.

class CategoryilstView(ListView):
    template_name = 'xanut.html'

    def get(self,request):
        categories = Category.objects.all()
        return render(request,self.template_name,{'categories':categories})


class CatgoryDetalView(DetailView):
    template_name = 'xanut_detal.html'

    def get(self,request,id):
        categoriesdetal = Category.objects.get(pk=id)
        return render(request,self.template_name,{'categoriesdetal':categoriesdetal})

# class SHoselistview(ListView):
#     template_name = 'xanut_detal.html'
    
#     def get(self,request):
#         shoseview = 
