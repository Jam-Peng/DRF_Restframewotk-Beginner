from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity =  models.IntegerField()
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.name)
    
