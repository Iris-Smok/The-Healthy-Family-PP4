""" Test for views.py """
# pylint: disable=locally-disabled, no-member
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestUser(TestCase):
    """ user """
    def test_user(self):
        """ user """
        test_user = User.objects.create_user(
            username='testuser', password='12345'
            )
        self.post = Post.objects.create(title='Test', author=test_user)
        self.comment = Comment.objects.create(
            body='Test Comment', post=self.post
            )
        self.client.login(username="testuser", password="12345")


class TestGetPages(TestCase):
    """ tests to ensure all the pages are displayes"""
    def test_get_home_page(self):
        """
        Get home page test
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_all_recipes_page(self):
        """
        Get all recipes page
        """
        response = self.client.get('/all_recipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_recipes.html')

    def test_get_fav_recipes_page(self):
        """
        Fav recipes page
        """
        response = self.client.get('/favourite_recipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favourite_recipes.html')

    def test_get_your_recipes_page(self):
        """
        Your recipes page
        """
        response = self.client.get('/your_recipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'your_recipes.html')

    def test_get_add_recipes_page(self):
        """
        Add recipes page
        """
        response = self.client.get('/add_recipe')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_recipe_details_page(self):
        """
        test recipe details page display as expacted
        """
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get(f'/recipe_details/{self.post.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'recipe_details.html')

    def test_edit_recipe_page(self):
        """
        edit recipe page display as expected
        """
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get(f'/edit_recipe/{self.post.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'edit_recipe.html')

    def test_edit_comment_page(self):
        """
        edit comment page display as expected
        """
        comments = Comment.objects.all()
        for comment in comments:
            response = self.client.get(f'/edit_comment/{self.comment.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'edit_comment.html')

    def test_search_page(self):
        """
        search page display as expected
        """
        response = self.client.get('/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')