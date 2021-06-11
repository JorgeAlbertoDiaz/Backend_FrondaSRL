from django.urls import path
from .views import UsuarioDetailView, UsuarioListView, EmpresaDetailView,EmpresaListView,SucursalListView, SucursalDetailView

urlpatterns = [
	path('usuario/', UsuarioListView.as_view(), name='lista_usuarios'),
	path('usuario/<int:pk>', UsuarioDetailView.as_view(), name='usuario'),
	path('empresa/', EmpresaListView.as_view(), name='lista_empresas'),
	path('empresa/<int:pk>', EmpresaDetailView.as_view(), name='empresa'),
	path('sucursal/', SucursalListView.as_view(), name='lista_sucursales'),
	path('sucursal/<int:pk>', SucursalDetailView.as_view(), name='sucursal'),
]