from django.contrib import admin
from .models import Course, Step


# Add a form
class StepInLine(admin.StackedInline):
    model = Step


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInLine, ]


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Step)
