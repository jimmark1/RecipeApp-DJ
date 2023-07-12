from django.shortcuts import render
from django.views import View

from . models import Recipe

class HomeView(View):
    def get(self, request):

        qs = Recipe.objects.all()
        context = {
            'data' : qs
        }

        return render(request, 'home/index.html', context)
    
    def post(self, request):
        pass