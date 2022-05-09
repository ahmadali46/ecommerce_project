from django.contrib import admin
from . models import *

# admin.site.register(RegisterModel)
@admin.register(RegisterModel)
class PersonAdmin(admin.ModelAdmin):
    
    list_display = ['username','lastname','email']
    
admin.site.register(Worker)
admin.site.register(Machine)

admin.site.register(OneCustomer)
admin.site.register(oneVehicle)

admin.site.register(ManyCustomer)
admin.site.register(ManyVehicle)
# Register your models here.

