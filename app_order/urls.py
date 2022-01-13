from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('order-list/', views.OrderList.as_view(), name='order-list'),
    path('order-detail/<str:pk>/', views.orderDetail, name="order-detail"),
    path('order-create/', views.orderCreate, name="order-Create"),
    path('order-update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order-delete/<str:pk>/', views.orderDelete, name="order-delete")
]
