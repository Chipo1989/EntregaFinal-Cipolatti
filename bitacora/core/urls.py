from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    # Tareas
    path('tareas/', views.lista_tareas, name='tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/editar/<int:pk>/', views.editar_tarea, name='editar_tarea'),
    path('tareas/eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),

    # Stock
    path('stock/', views.lista_stock, name='stock'),
    path('stock/crear/', views.crear_stock, name='crear_stock'),
    path('stock/editar/<int:pk>/', views.editar_stock, name='editar_stock'),
    path('stock/eliminar/<int:pk>/', views.eliminar_stock, name='eliminar_stock'),
]