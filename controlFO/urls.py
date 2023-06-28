from django.urls import path
import controlFO.views as views

urlpatterns = [
    path('app/', views.index, name='index'),
    path('form/', views.form, name='form'),
]
