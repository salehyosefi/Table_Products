from django.contrib import admin
from .models import TableProduct

#class AdminMode(admin.ModelAdmin):
#    list_display = ['name', 'price', 'date']
#    search_fields = ['name', 'price']

admin.site.register(TableProduct)

# Register your models here.
