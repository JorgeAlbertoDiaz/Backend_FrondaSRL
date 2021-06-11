# from django.shortcuts import render
from django.views import View
from .models import Usuario,Empresa,Sucursales
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.authtoken.models import Token

# Create your views here
class UsuarioListView(View):
	def get(self,request):

		# Filtro

		if('usuario_nombre' in request.GET):
			usuarios = Usuario.objects.filter(usuario_nombre__contains=request.GET['usuario_nombre'])	
		else:
			usuarios = Usuario.objects.all()
		return JsonResponse(list(usuarios.values()),safe=False)
	# def post(self,request):
	# 	# post ...
	# 	pass
	# def put(self,request):
	# 	# put ...
	# 	pass
	# def delete(self,request):
	# 	# delete ...
	# 	pass

class UsuarioDetailView(View):
	def get(self,request,pk):
		usuario = Usuario.objects.get(pk=pk)
		return JsonResponse(model_to_dict(usuario),safe=False)
	# def post(self,request):
	# 	# post ...
	# def put(self,request):
	# 	# put ...
	# def delete(self,request):
	# 	# delete ..


class EmpresaListView(View):
	def get(self,request):

		# Filtro

		if('usuario_nombre' in request.GET):
			empresas = Empresa.objects.filter(usuario_nombre__contains=request.GET['razon_social'])	
		else:
			empresas = Empresa.objects.all()
		return JsonResponse(list(empresas.values()),safe=False)
class EmpresaDetailView(View):
	def get(self,request,pk):
		empresa = Empresa.objects.get(pk=pk)
		return JsonResponse(model_to_dict(empresa),safe=False)

class SucursalListView(View):
	def get(self,request):

		# Filtro

		if('usuario_nombre' in request.GET):
			sucursales = Sucursales.objects.filter(usuario_nombre__contains=request.GET['nombre_sucursal'])	
		else:
			sucursales = Sucursales.objects.all()
		return JsonResponse(list(sucursales.values()),safe=False)
class SucursalDetailView(View):
	def get(self,request,pk):
		sucursales = Sucursales.objects.get(pk=pk)
		return JsonResponse(model_to_dict(sucursales),safe=False)