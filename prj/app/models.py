from django.db import models
from django.contrib.auth.models import User


class Kategorie(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev


class Recept(models.Model):
    nazev = models.CharField(max_length=200)
    popis = models.TextField()
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazev


class Ingredience(models.Model):
    nazev = models.CharField(max_length=100)
    recepty = models.ManyToManyField(Recept)

    def __str__(self):
        return self.nazev


class Postup(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    krok = models.TextField()
    poradi = models.IntegerField()

    def __str__(self):
        return f"{self.recept} - {self.poradi}"


class Hodnoceni(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    hodnota = models.IntegerField()

    def __str__(self):
        return f"{self.recept} - {self.hodnota}"