from django.contrib import admin

# Register your models here.
from .models import Team_Lead,Myform,Multi_File

admin.site.register(Team_Lead)
admin.site.register(Myform)
admin.site.register(Multi_File)