from django.http import HttpResponse
from . models import Student


def student(request):
    students = Student.objects.all()
    return HttpResponse(students)

def faculty(request):
    faculties = faculty.objects.all()
    return HttpResponse(faculties)

def course(request):
    courses = course.objects.all()
    return HttpResponse(courses)



