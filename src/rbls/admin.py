from django.contrib import admin
from .models import Rbllist

admin.site.register(Rbllist, list_display = ['name'])