from django.contrib import admin
from .models import *
# Register your models here.
from .models import Party

admin.site.register(Party)

admin.site.register(Apps)
admin.site.register(Banks)

class PartyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
   
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()