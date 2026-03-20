from django.db import models

# Create your models here.
class Recept(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

class Comment(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
