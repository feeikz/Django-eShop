from django.urls import path
from . import views

app_name="shop"

urlpatterns = [
    url('', views.product_list, name='product_list'),
    url('<str:category_slug>/',views.product_list, name='product_list_by_category'),
    url('<int:id>/<str:slug>/',views.product_detail, name='product_detail'),

      
]
