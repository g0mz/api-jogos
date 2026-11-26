from django.db import models


class Jogo(models.Model):
    titulo = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=100)
    ano = models.IntegerField()
    zerado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
