
from django.contrib import admin
from django.urls import path
from app.views import student, view_student, add_student, delete_student,update_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',student, name='student' ),
    path('view_student/', view_student, name='view_student'),
    path('add_student/',add_student, name='add_student'),
    path('delete_student/<int:pid>/', delete_student, name='delete_student'),
    path('update_student/<int:id>/', update_student, name='update_student')
  ]
