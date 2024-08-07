from django.contrib import admin

# Register your models here.

from . models import User, Recipe, Procedure, Like, Comment

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Like)
