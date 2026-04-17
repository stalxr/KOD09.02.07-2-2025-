from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.partner_list, name='partner_list'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('partners/', views.partner_list, name='partners'),
    path('partners/<int:pk>/', views.partner_detail, name='partner_detail'),
    path('partners/add/', views.partner_add, name='partner_add'),
    path('partners/<int:pk>/edit/', views.partner_edit, name='partner_edit'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('history/', views.sales_history, name='sales_history'),
]
