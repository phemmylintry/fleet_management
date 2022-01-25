from django.contrib import admin
from .models import Flight, Aircraft, Airport


admin.site.register(Flight)
admin.site.register(Aircraft)
admin.site.register(Airport)