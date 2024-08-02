from django.shortcuts import render
from .models import Student 

# Display a list of all students

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/list.html',{'students':students})


# Display a single student

def student_detail(request,id):
    student = Student.objects.get(id=id)

    return render(request, 'student/detail.html',{'student':student})
    