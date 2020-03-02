from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from .models import *

# Checkbox for many-to-many fields
class FilmotekaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Film, FilmotekaAdmin)
admin.site.register(Genre)

