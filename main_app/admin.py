from django.contrib import admin

from .models import Banger, Listening, Playlist

# Register your models here.

admin.site.register(Banger)
admin.site.register(Listening)
admin.site.register(Playlist)