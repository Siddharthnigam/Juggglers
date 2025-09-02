from django.urls import path
from . import admin_views

urlpatterns = [
    path('users/', admin_views.AdminUserListView.as_view(), name='admin-users'),
    path('users/<int:pk>/', admin_views.AdminUserUpdateView.as_view(), name='admin-user-update'),
]