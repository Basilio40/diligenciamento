from django.contrib import admin
from proposta import models
from django.utils.html import format_html

# Register your models here.

class SevicoPropostaAdmin(admin.TabularInline):
    model = models.ServicoProposta

class PropostaAdmin(admin.ModelAdmin):
    def my_url_field(self, obj):
        return format_html('<a href="{}" target="_blank">Gerar Relatório</a>'.format('/proposta/relatorio/?proposta=' + str(obj.id)))
    my_url_field.allow_tags = True
    my_url_field.short_description = 'Link'

    model = models.Proposta
    list_display = ('id','my_url_field')
    search_fields = ('id',)
    inlines = [SevicoPropostaAdmin ]

admin.site.register(models.Proposta, PropostaAdmin)