"""
Views.py
"""
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic, View
from .models import Recipe


class HomePage(View):
    """
    Home page view
    view for last added recipes and most loved recipes sections
    """

    def get(self, request):
        """ get request """
        recipes = Recipe.objects.order_by('-published_on')[:4]
        context = {
            "recipes": recipes,
        }
        return render(request, 'index.html', context)


class AllRecipes(generic.ListView):
    """
    all_recipes page
    """
    model = Recipe
    queryset = Recipe.objects.order_by('-published_on')
    template_name = 'all_recipes.html'
    paginate_by = 6


class RecipeDetails(View):
    """ Recipe details page """


class LogIn(TemplateView):
    """
    all_recipes view
    """
    template_name = 'login.html'


class Register(TemplateView):
    """
    all_recipes view
    """
    template_name = 'register.html'
