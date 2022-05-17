"""
models.py
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    """
    Recipe model
    """
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')  # noqa
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    comments = models.ManyToManyField(User, related_name='blog_comments', blank= True)  # noqa

    class Meta:
        """
        ordering
        """
        ordering = ['-published_on']

    def __str__(self):
        """ string title """
        return self.title

    def number_of_likes(self):
        """ return total number of likes """
        return self.likes.count()

    def number_of_comments(self):
        """ return comment count """
        return self.comments.count()


class Comment(models.Model):
    """
    Comment class
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments_recipe_name')  # noqa
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_name')  # noqa
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_name')  # noqa
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        """
        ordering
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
