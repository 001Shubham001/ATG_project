from django.urls import path
from . import views

urlpatterns = [
    
path('', views.index, name='index.html'),
path('login/', views.login_view, name='login_view'),
path('register/', views.register, name='register'),
path('doctor/', views.doctor, name='doctor'),
path('patient/', views.patient, name='patient'),
path('admin/', views.admin, name='admin'),

]
