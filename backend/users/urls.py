from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views, admin_views
from .custom_jwt_views import CustomTokenObtainPairView
from .address_views import AddressListCreateView, AddressDetailView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('../addresses/', AddressListCreateView.as_view(), name='addresses'),
    path('../addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
]