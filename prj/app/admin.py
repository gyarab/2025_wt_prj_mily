from django.contrib import admin
from .models import Kategorie, Recept, Ingredience, Postup, Hodnoceni


@admin.register(Kategorie)
class KategorieAdmin(admin.ModelAdmin):
    pass


@admin.register(Recept)
class ReceptAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredience)
class IngredienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Postup)
class PostupAdmin(admin.ModelAdmin):
    pass


@admin.register(Hodnoceni)
class HodnoceniAdmin(admin.ModelAdmin):
    pass