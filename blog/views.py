from django.shortcuts import render
from blog.models import Articulo
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.
def articulo_lista(request):
    articulos = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/articulo_lista.html', {'articulos':articulos})
    
def articulo_detalle(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'blog/articulo_detalle.html', {'articulo': articulo})
