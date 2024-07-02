from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('about/', views.about, name='about'),
    path('crear_guitar/', views.crear_guitar, name='crear_guitar'),
    path('guitars/', views.guitars,name='guitars'),
    path('eliminar/<int:pk>', views.EliminarGuitar.as_view(),name='eliminar_guitar'),
    path('editar/<int:pk>/', views.EditarGuitar.as_view(), name='editar_guitar'),
    path('ver/<int:pk>', views.VerGuitar.as_view(),name='ver_guitar'),
]
