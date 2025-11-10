from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('shop/', views.shop, name="shop"),
    path('category/<int:category_id>/', views.shop, name="shop_by_category"),
    path('product_details/<int:id>/', views.product_details, name="product_details"),
    path('<int:category_id>/', views.shop, name='shop') 

]
