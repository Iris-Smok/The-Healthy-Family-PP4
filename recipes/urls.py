
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
    path('edit_comment/<int:pk>',
         views.EditComment.as_view(), name='edit_comment'),
    path('delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    path('your_recipes', views.YourRecipes.as_view(), name='your_recipes'),
    path('add_recipe', views.AddRecipe.as_view(), name='add_recipe'),
    path('edit_recipe/<int:pk>',
         views.EditRecipe.as_view(), name='edit_recipe'),
]
