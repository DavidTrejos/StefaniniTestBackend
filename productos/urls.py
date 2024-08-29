from django.urls import path
from . import views

urlpatterns = [
    path('register_inventory/', views.register_inventory, name='register_inventory'),
    path('list_inventory/', views.list_inventory, name='list_inventory'),
    path('deliver_product/<str:product_name>/', views.deliver_product, name='deliver_product'),
    path('list_product_types/', views.list_product_types, name='list_product_types'),
    path('update_product/<str:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<str:product_id>/', views.delete_product, name='delete_product'),
]
