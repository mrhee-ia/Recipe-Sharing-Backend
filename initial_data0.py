import os
import sys
import django

sys.path.append('/Volumes/Cristina/Programming/Personal Projects/RecipeSharingProject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RSProject.settings')
django.setup()

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from RSBase.models import User, Recipe

content_type = ContentType.objects.get_for_model(Recipe)

# Create Groups
author_group, created = Group.objects.get_or_create(name='Authors')
viewer_group, created = Group.objects.get_or_create(name='Viewers')

# Create Permissions
edit_recipe_perm = Permission.objects.create(
    codename='edit_recipe',
    name='Can edit recipe',
    content_type=content_type,
)
like_recipe_perm = Permission.objects.create(
    codename='like_recipe',
    name='Can like recipe',
    content_type=content_type,
)
comment_recipe_perm = Permission.objects.create(
    codename='comment_recipe',
    name='Can comment recipe',
    content_type=content_type,
)

try:
    edit_recipe_perm = Permission.objects.get(codename='edit_recipe')
    like_recipe_perm = Permission.objects.get(codename='like_recipe')
    comment_recipe_perm = Permission.objects.get(codename='comment_recipe')
except Permission.DoesNotExist:
    print("Permissions 'edit, like, and comment' does not exist.")

# Create Users
user1 = User.objects.create_user(
    username='blabberbast',
    email='unicapsylesbur@gmail.com',
    password='annyeong1',
    first_name='Unica',
    last_name='Psylesbur',
    country='PH'
)

user2 = User.objects.create_user(
    username='areeyahs',
    email='songyuqiganda@gmail.com',
    password='annyeong2',
    first_name='Song',
    last_name='Yuqi',
    country='PH'
)

# Add Groups and Permissions to Users
user1.groups.add(author_group, viewer_group)
user1.user_permissions.add(edit_recipe_perm, like_recipe_perm, comment_recipe_perm)

user2.groups.add(viewer_group)
user2.user_permissions.add(like_recipe_perm, comment_recipe_perm)

print("Data has been populated successfully.")
