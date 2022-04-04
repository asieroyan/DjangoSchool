from django.contrib import admin

from .models import Class, Student


# Register your models here.
class ClassAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
