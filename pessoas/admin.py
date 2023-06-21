from django.contrib import admin

# Register your models here.
from .models import Pessoa
# Register your models here.

class ListandoPessoa(admin.ModelAdmin):
    list_display = [
        'id','nome','email'
    ]
    list_display_links = [
        'id','nome',
    ]
    search_fields = ['nome']
    list_editable = ['email']
    ordering = ['-id',]
    list_filter = ['nome']
    list_per_page = 7
admin.site.register(Pessoa, ListandoPessoa)
