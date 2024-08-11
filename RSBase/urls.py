from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, RecipeViewSet, ProcedureViewSet, LikeViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'procedures', ProcedureViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]