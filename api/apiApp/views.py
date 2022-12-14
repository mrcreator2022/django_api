from http.client import HTTPResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

#single user date

def student_detail(request):
    stu = Student.objects.get(id =1)
    serializer =StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HTTPResponse(json_data, content_type='application/json')
