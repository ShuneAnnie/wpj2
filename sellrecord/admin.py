from django.contrib import admin
from .models import Sellrecord 
# Register your models here.

admin.site.site_header = 'Waaneiza sellrecord Management system'

class SellrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'price','showroom','paid','date']
    list_filter = ['customer', 'customer_phone', 'price','showroom','paid','date']
    search

admin.site.register(Sellrecord, SellrecordAdmin)
