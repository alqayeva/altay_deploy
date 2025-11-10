from django.urls import path
from . import views
app_name = 'info'

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('error/', views.error, name = "error"),
    path('contact_view/', views.contact_view, name = "contact_view"),
    path('faq/', views.faq, name = "faq"),
    path('privacy_policy/', views.privacy_policy, name = "privacy_policy"),
    
]