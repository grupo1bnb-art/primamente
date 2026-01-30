from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from decimal import Decimal
import random

from .models import Usuario, Ruleta
from django.utils import timezone


# ===============================
# 🎮 ZONA DE JUEGOS
# ===============================
@login_required(login_url='login')
def juegos(request):

    juegos = [
        {
            'nombre': 'Ruleta',
            'icono': '🎡',
            'estado': 'Disponible'
        },
        {
            'nombre': 'Tragamonedas',
            'icono': '🎰',
            'estado': 'Próximamente'
        },
        {
            'nombre': 'Cartas',
            'icono': '🃏',
            'estado': 'Próximamente'
        },
        {
            'nombre': 'Dados',
            'icono': '🎲',
            'estado': 'Próximamente'
        },
    ]

    return render(request, 'inverso_sa/juegos.html', {
        'juegos': juegos
    })

@login_required
def ruleta_view(request):
    return render(request, 'inverso_sa/ruleta.html')


# ===============================
# 🎰 RULETA CASINO
# ===============================
@login_required
def jugar_ruleta(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método inválido"})

    monto = Decimal(request.POST.get("monto", 0))
    usuario = request.user

    if monto <= 0:
        return JsonResponse({"error": "Monto inválido"})

    if usuario.saldo < monto:
        return JsonResponse({"error": "Saldo insuficiente"})

    # 🎰 CONFIG CASINO
    probabilidad_ganar = 35  # %
    multiplicador = Decimal("1.5")

    numero = random.randint(1, 100)

    if numero <= probabilidad_ganar:
        # ✅ GANA
        ganancia = monto * multiplicador
        usuario.saldo += ganancia
        resultado = "GANÓ"
    else:
        # ❌ PIERDE
        usuario.saldo -= monto
        ganancia = -monto
        resultado = "PERDIÓ"

    usuario.save()

    Ruleta.objects.create(
        usuario=usuario,
        apuesta=monto,
        resultado=resultado,
        ganancia=ganancia
    )

    return JsonResponse({
        "resultado": resultado,
        "ganancia": float(ganancia),
        "saldo": float(usuario.saldo)
    })


def error_403(request, exception=None):
    """
    Vista personalizada para manejar errores 403
    """
    return render(request, "inverso_sa/forbidden.html", {
        "mensaje": "⚠️ Por favor presiona el botón de ingresar solo una vez y espera mientras el sistema carga."
    })