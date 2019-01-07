from django.contrib import admin

from django.db.models import Sum

from .models import Country, City

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(City)
class Cityadmin(admin.ModelAdmin):
	list_display = ('name', 'country', 'population','total')


