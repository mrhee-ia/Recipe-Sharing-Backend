import os
import sys
import django

sys.path.append('/Volumes/Cristina/Programming/Personal Projects/RecipeSharingProject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RSProject.settings')
django.setup()

from RSBase.models import Recipe, Procedure

recipe = Recipe.objects.get(title='Graham Balls')

procedure = Procedure.objects.create(
    procedure_recipe = recipe,
    name = 'Third Step',
    step = 'Get a portion and mold it into a circle with your hands.'
)

print("Data has been populated successfully.")