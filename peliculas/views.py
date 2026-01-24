from django.shortcuts import render
from typing import Dict, Any
from .services import ver_peliculas, ver_pagina

# Create your views here.
def inicio(request):
    parametros: Dict [str, str] = {
        'genres': '28',
        'page': '1',
        
        
    }
    
    datos: Dict[str, Any] = {
        'titulo' : 'Portal de peliculas',
        'encabezado' : 'Listado de peliculas',
        'peliculas' : ver_peliculas(parametros),
        'images': 'https://image.tmdb.org/t/p/w500',
        'pagina': ver_pagina(parametros),
        
    }
    return render(request, 'peliculas/index.html', datos)

def anterior(request, page):
    parametros: Dict [str, str] = {
        'genres': '28',
        'page': page,
        
        
    }
    
    datos: Dict[str, Any] = {
        'titulo' : 'Portal de peliculas',
        'encabezado' : 'Listado de peliculas',
        'peliculas' : ver_peliculas(parametros),
        'images': 'https://image.tmdb.org/t/p/w500',
        'pagina': ver_pagina(parametros),
        
    }
    return render(request, 'peliculas/index.html', datos)



def siguiente(request, page):
    parametros: Dict [str, str] = {
        'genres': '28',
        'page': page,
        
        
    }
    
    datos: Dict[str, Any] = {
        'titulo' : 'Portal de peliculas',
        'encabezado' : 'Listado de peliculas',
        'peliculas' : ver_peliculas(parametros),
        'images': 'https://image.tmdb.org/t/p/w500',
        'pagina': ver_pagina(parametros),
        
    }
    return render(request, 'peliculas/index.html', datos)
