from django.contrib import admin
from .models import *
# Register your models here.
from .models import Party



admin.site.register(Apps)
admin.site.register(Banks)

class PartyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner','apps','isApproved')
   
   
    
admin.site.register(Party,PartyAdmin)
