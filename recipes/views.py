"""
Views.py
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import UpdateView, CreateView
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm, RecipeForm


class HomePage(View):
    """
    Home page view
    view for last added recipes and most loved recipes sections
    """

    def get(self, request):
        """ get request """
        posts = Post.objects.order_by('-published_on')[:4]
        context = {
            "posts": posts,
        }
        return render(request, 'index.html', context)


class AllRecipes(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'all_recipes.html'
    paginate_by = 6


class RecipeDetails(View):
    """ Recipe details page """

    def get(self, request, slug):
        """What happens for a GET request"""
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments_post_name.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug):
        """What happens for a POST request"""
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments_post_name.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('recipe_details', args=[slug]))
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class EditComment(UpdateView):
    """ Edit Comments """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm


def delete_comment(request, comment_id):
    """Deletes comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse(
        'recipe_details', args=[comment.post.slug]))


class RecipeLike(View):
    """
    like and unlike post class
    """
    def post(self, request, slug):
        """
        like and unlike posts
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class YourRecipes(View):
    """ view for user recipes page"""
    def get(self, request):
        """your_recipes view, get method"""
        post = Post.objects.filter(author=request.user)

        paginator = Paginator(post, 6)  # Show 6 recipes per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'your_recipes.html', {"page_obj": page_obj, })


class AddRecipe(View):
    """ add recipe"""
    def get(self, request):
        """What happens for a GET request"""
        return render(request, "add_recipe.html", {"recipe_form": RecipeForm()})

    def post(self, request):
        """What happens for a POST request"""
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify('-'.join([recipe.title, str(recipe.author)]), allow_unicode=False)
            recipe.save()
            return redirect('your_recipes')
        else:
            # create message error to complete all the fields
            recipe_form = RecipeForm()

        return render(
            request,
            "add_recipe.html",
            {
                "recipe_form": recipe_form

            },
        )

class EditRecipe(UpdateView):
    """ Edit Recipe """
    model = Post
    template_name = 'edit_recipe.html'
    form_class = RecipeForm


# def delete_comment(request, comment_id):
#     """Deletes comment"""
#     comment = get_object_or_404(Comment, id=comment_id)
#     comment.delete()
#     return HttpResponseRedirect(reverse(
#         'recipe_details', args=[comment.post.slug]))