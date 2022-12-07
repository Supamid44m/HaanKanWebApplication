from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Party)
admin.site.register(Apps)
admin.site.register(AppImage)
admin.site.register(QrcodePayment)