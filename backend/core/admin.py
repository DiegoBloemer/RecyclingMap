from django.contrib import admin
from .models import LocalReciclagem, Imagem, TipoResiduo, User

# Register your models here.

admin.site.register(LocalReciclagem)
admin.site.register(Imagem)
admin.site.register(TipoResiduo)
admin.site.register(User)