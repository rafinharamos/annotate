from django.db import models

from django.db.models import Sum

class Country(models.Model):
    name = models.CharField(max_length=30)

@property    
def __call__(self):
    totalizador = City.objects.values('country__name').annotate(Sum('population'))
    return self.totalizador	


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)
    population = models.PositiveIntegerField()
    total = property(__call__)


    def __str__(self):
        return self.country

    