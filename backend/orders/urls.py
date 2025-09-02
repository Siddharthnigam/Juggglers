from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='user-orders'),
    path('create/', views.CreateOrderView.as_view(), name='create-order'),
    path('admin/', views.AdminOrderListView.as_view(), name='admin-orders'),
    path('admin/<int:pk>/', views.AdminOrderUpdateView.as_view(), name='admin-order-update'),
]