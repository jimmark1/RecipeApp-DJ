from django.urls import path
from . views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/<str:id>/', RecipeView.as_view(), name='recipe'),

    path('about/', AboutView.as_view(), name='about'),
]