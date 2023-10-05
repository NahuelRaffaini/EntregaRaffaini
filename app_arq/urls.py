from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('crear_proyecto/', ProyectoCreateView.as_view(), name='crear_proyecto'),
    path('actualizar_proyecto/<pk>', ProyectoUpdateView.as_view(), name='actualizar_proyecto'),
    path('eliminar_proyecto/<pk>', ProyectoDeleteView.as_view(), name='eliminar_proyecto'),
    path('lista_proyecto/', ProyectoListView.as_view(), name='lista_proyecto'),
    path('filtrar_proyectos/', filtrar_proyectos, name='filtrar_proyectos'),
]