from django.contrib import admin
from .models import Experience

# Register your models here.


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'organization', 'designation', 'to', '_from']
    list_display_links = ['id', 'organization', 'designation']
    list_filter = ['designation']
    search_fields = ['organization', 'designation']


admin.site.register(Experience, ExperienceAdmin)
