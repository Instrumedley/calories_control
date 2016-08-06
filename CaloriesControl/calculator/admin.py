from django.contrib import admin

from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','unity','calories_per_unity')

admin.site.register(Food, FoodAdmin)
