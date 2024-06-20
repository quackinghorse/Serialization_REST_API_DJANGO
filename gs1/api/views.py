from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

def Studentdetail(requests,pk):
    try:
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    except Student.DoesNotExist:
        return HttpResponse("Student not found", status=404)
    
def Studentlist(requests):
    try:
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    except Student.DoesNotExist:
        return HttpResponse("Student not found", status=404)

