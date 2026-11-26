from django.urls import path

from . import views

urlpatterns = [
    path("", views.pagina),
    path("api/jogos/", views.jogos),
    path("api/jogos/<int:id>/", views.jogo_detalhe),
]
