from django.db import models

class Post(models.Model):

    idPost = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    class Meta:

        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "Posts"

    def __str__(self):

        return self.titulo 
    
class Comentarios(models.Model):

    idComentario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    activo = models.BooleanField(default=True)
    fkPost = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="comentarios")

    class Meta:

        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        db_table = "Comentarios"

    def __str__(self):

        return self.nombre