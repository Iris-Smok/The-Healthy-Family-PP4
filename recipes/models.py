"""
models.py
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')  # noqa
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        ordering
        """
        ordering = ['-published_on']

    def __str__(self):
        """
        string title
        """
        return self.title

    def number_of_likes(self):
        """ return number of likes"""
        return self.likes.count()

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('your_recipes')


class Comment(models.Model):
    """
    Comment class
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_post_name')  # noqa
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        ordering
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('recipe_details', args=[self.post.slug])
