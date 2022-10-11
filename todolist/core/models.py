from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'