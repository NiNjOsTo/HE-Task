from django.contrib import admin
from .models import Package,Variant,Slot,Country,Currency,Date
# Register your models here.
admin.site.register(Package)
admin.site.register(Variant)
admin.site.register(Slot)
admin.site.register(Country)
admin.site.register(Currency)
admin.site.register(Date)