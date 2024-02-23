from django.contrib import admin
from .models import Post, Comentarios

class AdminPost(admin.ModelAdmin):

    search_fields = ('titulo', 'fecha',)
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ('fecha',)

admin.site.register(Post, AdminPost)


class AdminComentarios(admin.ModelAdmin):

    search_fields = ('nombre', 'fecha',)
    readonly_fields = ('fecha',)

admin.site.register(Comentarios, AdminComentarios)