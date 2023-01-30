from django.db import models


class Expression(models.Model):
    rom = models.CharField(max_length=500)
    eng = models.CharField(max_length=500)

    def __str__(self):
        return self.rom
