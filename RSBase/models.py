from django.db import models

from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser



# Recipe Category choices
CATEGORY_CHOICES = [
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('appetizer', 'Appetizer'),
    ('salad', 'Salad'),
    ('side-dish', 'Side-Dish'),
    ('baked goods', 'Baked Goods'),
    ('dessert', 'Dessert'),
    ('snack', 'Snack'),
    ('soup', 'Soup'),
    ('vegetarian', 'Vegetarian'),
    ('fried', 'Fried'),
    ('bread', 'Bread'),
    ('seafood', 'Seafood'),
    ('pasta', 'Pasta'),
    ('cookies', 'Cookies'),
    ('ice cream', 'Ice Cream'),
    ('others', 'Others'),
]



class User(AbstractUser):   
    # using built-in User but modified
    username = models.CharField(max_length=60, unique=True, null=False)
    email = models.EmailField(max_length=225, unique=True, null=False)
    # password is already included
    first_name = models.CharField(max_length=225, null=False)
    last_name = models.CharField(max_length=225, null=False)
    # -----------------------------------------------------------------
    country = CountryField(null=False)
    # Optional in forms and can be NULL in the database
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=101, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username



class Recipe(models.Model):
    recipe_user = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE)
    title = models.CharField(max_length=225, null=False)
    description = models.TextField(null=False)
    rmedia = models.FileField(upload_to='recipe_media/', null=True, blank=True) # for both vid and img
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES, default='others')
    ingredients = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    


class Procedure(models.Model):
    procedure_recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=True)
    smedia = models.FileField(upload_to='step_media/', null=True, blank=True)
    step = models.TextField(null=False)
    step_order = models.PositiveIntegerField(null=False)
    
    class Meta:
        ordering = ['step_order']
        unique_together = ['procedure_recipe', 'step_order']
    
    def __str__(self):
        return f"{self.recipe.title} - {self.name}"



class Like(models.Model):
    like_recipe = models.ForeignKey(Recipe, related_name="like_recipe", on_delete=models.CASCADE)
    like_user = models.ForeignKey(User, related_name="like_user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['like_user', 'like_recipe']

    

class Comment(models.Model):
    comment_recipe = models.ForeignKey(Recipe, related_name="comments-recipe", on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, related_name="comments-user", on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="replies", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
