from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'home.html'
    
class IndexPage(TemplateView):
    template_name = 'index.html'
    
class AloqaPage(TemplateView):
    template_name = 'contact.html'