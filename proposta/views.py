from django import template
from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Proposta , ServicoProposta
from cadastro import models as cadastro_models
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/admin")
def proposta(request):
    proposta_id = request.GET.get("proposta")
    try:
        vendas = Proposta.objects.get(id=proposta_id)
        servicos = ServicoProposta.objects.filter(proposta=proposta)
    except:
        return HttpResponse("400 -  Bad Request.Venda inexistente.", status = 400)
    # OS = ServicoVenda.objects.all()
    # OS = request.GET.get("OS")
    template = loader.get_template("relatorio_proposta.html")
    total = 0
    # for item in servicos:
    #     total = total + item.preco_venda
    context = {

        "proposta": proposta,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
