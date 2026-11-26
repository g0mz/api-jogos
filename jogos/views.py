import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Jogo


def jogo_para_dict(jogo):
    return {
        "id": jogo.id,
        "titulo": jogo.titulo,
        "plataforma": jogo.plataforma,
        "ano": jogo.ano,
        "zerado": jogo.zerado,
    }


@csrf_exempt
def jogos(request):
    if request.method == "GET":
        lista = []
        for jogo in Jogo.objects.all().order_by("titulo"):
            lista.append(jogo_para_dict(jogo))
        return JsonResponse({"jogos": lista})

    if request.method == "POST":
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido."}, status=400)

        for campo in ["titulo", "plataforma", "ano"]:
            if not dados.get(campo):
                return JsonResponse(
                    {"erro": f"O campo {campo} é obrigatório."}, status=400
                )

        jogo = Jogo.objects.create(
            titulo=dados["titulo"],
            plataforma=dados["plataforma"],
            ano=dados["ano"],
        )
        return JsonResponse(jogo_para_dict(jogo), status=201)

    return JsonResponse({"erro": "Método não permitido."}, status=405)


@csrf_exempt
def jogo_detalhe(request, id):
    try:
        jogo = Jogo.objects.get(id=id)
    except Jogo.DoesNotExist:
        return JsonResponse({"erro": "Jogo não encontrado."}, status=404)

    if request.method == "GET":
        return JsonResponse(jogo_para_dict(jogo))

    if request.method == "PUT":
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido."}, status=400)

        jogo.titulo = dados.get("titulo", jogo.titulo)
        jogo.plataforma = dados.get("plataforma", jogo.plataforma)
        jogo.ano = dados.get("ano", jogo.ano)
        jogo.zerado = dados.get("zerado", jogo.zerado)
        jogo.save()
        return JsonResponse(jogo_para_dict(jogo))

    if request.method == "DELETE":
        jogo.delete()
        return HttpResponse(status=204)

    return JsonResponse({"erro": "Método não permitido."}, status=405)


def pagina(request):
    return render(request, "jogos/index.html")
