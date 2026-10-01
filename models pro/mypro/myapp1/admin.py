from django.contrib import admin
from .  models import Student, faculty,course

admin.site.register(Student)
admin.site.register(faculty)
admin.site.register(course)