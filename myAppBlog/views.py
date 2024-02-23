from django.shortcuts import render, redirect
from .models import Post, Comentarios
from .forms import FormularioComentarios

def index(request):

    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})


def detallePost(request, idPost):

    hola = Comentarios.objects.all()

    posts = Post.objects.get(idPost=idPost)

    if request.method == 'POST':

        form = FormularioComentarios(request.POST)

        if form.is_valid():

            nom = form.cleaned_data.get('nombre')
            em = form.cleaned_data.get('email')
            con = form.cleaned_data.get('contenido')
            act = form.cleaned_data.get('activo')
            fk = form.cleaned_data.get('fkPost')


            comentarios = Comentarios.objects.create(
            
                nombre = nom,
                email = em,
                contenido = con,
                activo = act,
                fkPost = fk,

            )

            comentarios.save()
            form = FormularioComentarios()
            
            

    else:

        form = FormularioComentarios()

    modulos = {'posts': posts, 'form': form, 'hola': hola}

    return render(request, 'detallePost.html', modulos)