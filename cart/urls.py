from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url('', views.cart_detail, name='cart_detail'),
    url('add/<product_id>/', views.cart_add, name='cart_add'),
    url('remove/<product_id>/', views.cart_remove, name='cart_remove'),
]
