from django.contrib import admin

# Register your models here.

from .models import Musician, Album, Person

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Person)