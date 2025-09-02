from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .wishlist_views import WishlistView

router = DefaultRouter()
router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Separate wishlist URLs
wishlist_urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]

urlpatterns += wishlist_urlpatterns