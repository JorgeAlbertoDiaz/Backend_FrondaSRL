from django.urls import path
from .views import UsuarioDetailView, UsuarioListView

urlpatterns = [
	path('usuario/', UsuarioListView.as_view(), name='lista_usuarios'),
	path('usuario/<int:pk>', UsuarioDetailView.as_view(), name='usuario')
]