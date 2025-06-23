from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('printing/', views.printing_view, name='printing'),
    path('modeling/', views.modeling_view, name='modeling'),
    path('scanning/', views.scanning_view, name='scanning'),
    path('contact/', views.contact_view, name='contact'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
]
