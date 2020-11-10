from django.contrib import admin
from .models import Pack, Component, PackComponent


admin.site.register(Pack)
admin.site.register(Component)
admin.site.register(PackComponent)

