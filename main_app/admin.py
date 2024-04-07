from django.contrib import admin
from .models import Specie, Bird, Feeding
# Register your models here.


# Register your models here
admin.site.register(Bird)
admin.site.register(Feeding)
admin.site.register(Specie)