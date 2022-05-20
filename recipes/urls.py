
"""
recipes urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('all_recipes', views.AllRecipes.as_view(), name='all_recipes'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name="recipe_details"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),

]
