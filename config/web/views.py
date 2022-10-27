from django.shortcuts import render
from web.formularios.formularioPersonal import FormularioPersonal

#importar el formulario a render
from web.formularios.formularioPlatos import FormularioPlatos

# Create your views here.
#las vistas en django son los CONTROLADORES

#Las vistas son funciones de python 

def Home(request):
    return render(request,'index.html')

def Platos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario
    }

    return render(request,'platos.html',datosParaTemplate)

def Personal(request):

    formulario=FormularioPersonal()
    datosParaTemplate={
        'formularioRegistroPersonal':formulario
    }


    return render(request,'personal.html',datosParaTemplate)
