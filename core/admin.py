from django.contrib import admin

# Register your models here.
from .models import Chamado

# Isso faz o modelo "Chamado" aparecer no /admin
admin.site.register(Chamado)