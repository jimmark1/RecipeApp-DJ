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
    
class RecipeView(View):
    def get(self, request, id):

        qs = Recipe.objects.get(id=id)

        context = {
            'data' : qs,
            'ingredients': qs.recipe_ingredients.split(','),
        }

        return render(request, 'recipe/recipe.html', context)
    

class AboutView(View):
    def get(self, request):
        return render(request, 'about/about.html')