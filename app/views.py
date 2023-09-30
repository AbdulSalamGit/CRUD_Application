from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app.models import Student
from django.urls import reverse


def student(request):
    return render(request, "base.html")


def view_student(request):
    students = Student.objects.all()
    return render(request, "view_student.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        cn = request.POST.get("class_name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        try:
            Student.objects.create(
                first_name=fn, last_name=ln, class_name=cn, age=age, grade=grade
            )
            error = "no"
        except:
            error = "yes"
        return HttpResponseRedirect(reverse("view_student"))

    return render(request, "add_student.html")


def delete_student(request, pid):
    student = Student.objects.get(id=pid)
    student.delete()
    return redirect("view_student")


def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        # Process the form data and update the student object
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.class_name = request.POST.get("class_name")
        student.age = request.POST.get("age")
        student.grade = request.POST.get("grade")
        student.save()

        return redirect("view_student")

    return render(request, "update_student.html", {"student": student})
