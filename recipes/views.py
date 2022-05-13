"""
Views.py
"""
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.db.models import Count
from .models import Post


class HomePage(View):
    """
    Home page view
    view for last added recipes and most loved recipes
    """

    def get(self, request):
        """
        get request
        """
        posts = Post.objects.order_by('-published_on')[:4]
        context = {
            "posts": posts,
        }
        return render(request, 'index.html', context)


class AllRecipes(TemplateView):
    """
    all_recipes view
    """
    template_name = 'all_recipes.html'


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
