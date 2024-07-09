from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




urlpatterns = [
	path('', inicio, name="inicio"),
	path('NoticiaPrincipal/',NoticiaPrincipal, name="NoticiaPrincipal"),
	path('Noticia1/', Noticia1, name="Noticia1"),
	path('Noticia2/', Noticia2, name="Noticia2"),
	path('Noticia3/', Noticia3, name="Noticia3"),
	path('deportes/', deportes, name="deportes"),
	path('undiacomohoy/', undiacomohoy, name="undiacomohoy"),
	path('calendario/', calendario, name="calendario"),
	path('contactanos/', contactanos, name="contactanos"),
	path('trabajaconnos/', trabajaconnos, name="trabajaconnos"),
	path('politics/', politics, name="politics"),
	path('baloncesto/', baloncesto, name="baloncesto"),
	path('futbol/', futbol, name="futbol"),
	path('golf/', golf, name="golf"), 
	path('tenis/', tenis, name="tenis"),        
	path('contactanos/', contactanos, name="contactanos"), 
	path('Palestino/', Palestino, name="Palestino"), 
	path('paagina_para_prueba/', paagina_para_prueba, name="paagina_para_prueba"), 
	path('nueva_noticia/', nueva_noticia, name="nueva_noticia"), 
	path('elimina/<str:pk>', elimina, name="elimina"), 
	path('agrega/', agrega, name="agrega"), 
	path('nuevo/', nuevo, name="nuevo"), 
	path('agrega_form/', agrega_form, name="agrega_form"), 
	path('Inicio_sesion/', Inicio_sesion, name="Inicio_sesion"), 
	path('valida', valida, name="valida"),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('salir', salir, name="salir"),
	path('login/', auth_views.LoginView.as_view(), name='login'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

