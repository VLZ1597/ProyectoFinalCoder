from django.db import models
from django.contrib.auth.models import User

class Guitar(models.Model):
    marca = models.CharField(max_length=20)
    forma = models.CharField(max_length=20)
    comentario = models.TextField() 
    load_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Guitar: {self.marca} {self.forma} - Comentario: {self.comentario}'

