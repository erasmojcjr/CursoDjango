from django.contrib import admin
from .models import Cliente, Telefone, CPF, Limitecredito, Banco

# Register your models here.

#fields
#list_display
#list_filter
#search_fields

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'cidade', 'uf')
    list_filter = ('cidade',)
    search_fields = ('id', 'nome')
    # fields = ('nome', 'endereco', 'cidade', 'uf') lista as filds que quer que apareça no formulario



admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Limitecredito)
admin.site.register(Banco)