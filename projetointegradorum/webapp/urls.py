from django.urls import path
from webapp import views
 
urlpatterns = [
    path('', views.home, name='meuapp-home'),
    path('faq/', views.faq, name='faq'),
    path('sobre/', views.sobre, name='sobre'),
    path('formulario1/', views.formulario1, name='formulario1'),
    path('formulario2/', views.formulario2, name='formulario2'),
 ]