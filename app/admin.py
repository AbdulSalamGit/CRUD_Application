from django.contrib import admin
from app.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'class_name', 'age', 'grade')  # Define the fields to display in the admin list view

admin.site.register(Student, StudentAdmin)  # Register the Student model with the StudentAdmin class
