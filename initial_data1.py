import os
import sys
import django

sys.path.append('/Volumes/Cristina/Programming/Personal Projects/RecipeSharingProject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RSProject.settings')
django.setup()

from RSBase.models import User, Recipe

# Fetch or create a User instance
user = User.objects.get(username='blabberbast')

recipe = Recipe.objects.create(
    recipe_user = user,
    title = 'Graham Balls',
    description = 'A no-bake treat made with crushed graham crackers, sweetened condensed milk, and various fillings. Perfect for snacking or sweet addition to any party.',
    category = 'snack',
    ingredients = '2 packages crushed graham crackers, 1 can sweetened condensed milk, 1 bag marshmallows'
)

print("Data has been populated successfully.")

