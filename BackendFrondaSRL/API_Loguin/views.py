# from django.shortcuts import render
from django.views import View
from .models import Usuario
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