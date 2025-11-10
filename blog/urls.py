

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog, name='blog'),    
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
]

