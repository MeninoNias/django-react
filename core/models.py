from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class List(models.Model):

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
