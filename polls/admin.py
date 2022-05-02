from django.contrib import admin

from polls.models import Project, Manager

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'is_good')
    search = ('name', )
    ordering = ('id', )

class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'birthday', 'gcount', 'bcount', 'proj_id')
    search_fields = ('name', )
    ordering = ('id', )

admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Manager, ManagerModelAdmin)