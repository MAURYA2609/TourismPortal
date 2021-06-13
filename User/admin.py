from django.contrib import admin
from .models import pBookings,hBookings

# Register your models here.
admin.site.register(pBookings)
admin.site.register(hBookings)