from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from .forms import *

# Create your views here.

def inicio(request):
    return render(request, 'core/inicio.html')

def NoticiaPrincipal(request):
    return render(request, 'core/NoticiaPrincipal.html')    

def Noticia1(request):
    return render(request, 'core/Noticia1.html')  

def Noticia2(request):
    return render(request, 'core/Noticia2.html')  

def Noticia3(request):
    return render(request, 'core/Noticia3.html')      

def deportes(request):
    return render(request, 'core/deportes.html')   

def undiacomohoy(request):
    return render(request, 'core/undiacomohoy.html')   

def calendario(request):
    return render(request, 'core/calendario.html')   
    
def contactanos(request):
    return render(request, 'core/contactanos.html')      

def trabajaconnos(request):
    return render(request, 'core/trabajaconnos.html')  

def politics(request):
    return render(request, 'core/politics.html')   

def baloncesto(request):
    return render(request, 'core/baloncesto.html')   

def futbol(request):
    return render(request, 'core/futbol.html') 

def golf(request):
    return render(request, 'core/golf.html') 

def tenis(request):
    return render(request, 'core/tenis.html') 

def contactanos(request):
    return render(request, 'core/contactanos.html') 

def Palestino(request):
    return render(request, 'core/Palestino.html')     

def paagina_para_prueba(request):
    return render(request, 'core/paagina_para_prueba.html') 
 

def nueva_noticia(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}

    return render(request, 'core/nueva_noticia.html', context) 

def elimina(request, pk):
    try:
        noticia = Noticia.objects.get(id=pk)
        noticia.delete()

        mensaje = 'Noticia eliminada'
        noticias = Noticia.objects.all()
        context = {'noticias': noticias, 'mensaje': mensaje}

        return render(request, 'core/nueva_noticia.html', context) 
    except:
        mensaje = 'Noticia no existente'
        noticias = Noticia.objects.all()
        context = {'noticias': noticias, 'mensaje': mensaje}

        return render(request, 'core/nueva_noticia.html', context) 

def agrega(request):
    return render(request, 'core/agrega.html') 
# def nuevo(request):
#     noticia = Noticia.objects.create(
#         titulo = request.POST["titulo"],
#         fecha = request.POST["fecha"],
#         descripcion = request.POST["descripcion"],
#         imagen = request.Files.get("imagen")
#     )

#     noticia.save()
#     mensaje = "Noticia agregada"

#     context = {'mensaje': mensaje}

#     return render(request, 'core/agrega.html', context) 

def nuevo(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = "Noticia agregada"
            return redirect('agrega')  # Redirige a la vista 'agrega' que tiene la URL con nombre 'agrega'
    else:
        form = NoticiaForm()

    context = {'form': form}
    return render(request, 'core/agrega_form.html', context)
def agrega_form(request):
    context = {
        "form": NoticiaForm()
    }

    return render(request, 'core/agrega_form.html', context) 

def Inicio_sesion(request):
    return render(request, 'core/Inicio_sesion.html')

def valida(request):
	user = request.POST["usuario"]
	psw = request.POST["password"]

	try:
		usuario = InicioSesion.objects.get(usuario = user, password = psw)
		request.session['usr'] = usuario.usuario
		mensaje = request.session['usr']
	except:
		mensaje = ''

	if 'usr' in request.session:
		mensaje = request.session['usr']

	context = {
		'mensaje': mensaje
	}

	return render(request, 'core/inicio.html', context)
   

def salir(request):
	del request.session['usr']
	return render(request, 'core/inicio.html')

def logout(request):
    return render(request, 'core/Inicio_sesion.html')