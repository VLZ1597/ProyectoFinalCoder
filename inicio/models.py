from django.db import models

class Guitar(models.Model):
    marca = models.CharField(max_length=20)
    forma = models.CharField(max_length=20) 
    
    def __str__(self):
        return f'Guitars cargadas: {self.marca} {self.forma} '