"""Unit Testing for Forms"""
from django.test import TestCase
from .forms import RecipeForm, CommentForm


class TestRecipeForm(TestCase):
    """Unit Test for Recipe Form"""

    def test_recipe_title_is_required(self):
        """ recipe title required"""
        form = RecipeForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_recipe_descriptio_is_required(self):
        """ recipe description required"""
        form = RecipeForm(({'description': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_recipe_ingredients_is_required(self):
        """ recipe ingredients required"""
        form = RecipeForm(({'ingredients': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(
            form.errors['ingredients'][0], 'This field is required.')

    def test_recipe_preparation_steps_is_required(self):
        """ recipe preparation steps required"""
        form = RecipeForm(({'preparation_steps': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('preparation_steps', form.errors.keys())
        self.assertEqual(
            form.errors['preparation_steps'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ form meta fields"""
        form = RecipeForm()
        self.assertEqual(
            form.Meta.fields, (
                'title', 'description', 'ingredients',
                'preparation_steps', 'image')
            )


class TestCommentForm(TestCase):
    """Test for Comments Form"""
    def test_post_title_is_required(self):
        """ comment form fields"""
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ form meta fields"""
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
