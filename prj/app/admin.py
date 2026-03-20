from django.contrib import admin
from .models import Recept, Comment

@admin.register(Recept)
class ReceptAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass