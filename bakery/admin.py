from django.contrib import admin

# Register your models here.
from bakery.models import Cake,Booking


admin.site.register(Cake)
admin.site.register(Booking)