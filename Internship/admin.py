from django.contrib import admin
from .models import Internship

# Register your models here.
admin.site.register(Internship)


from .models import Entreprise
admin.site.register(Entreprise)