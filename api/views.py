from django.shortcuts import render
from .serializers import LessonSerializer,ScheduleSerializer
from .models import Lesson,Schedule
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils import timezone

def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def dashboard(request):
    return render(request,"dashboard.html")
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def lesson(request):
    serializer = LessonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def lesson_check(request):
    now=timezone.localtime(timezone.now())
    # raise Exception(now)
    lesson=Lesson.objects.filter(user=request.user,is_opened=False,start_time__lte=now)
    if lesson.exists():
        data=[{"zoom_link": dars.link,"name": dars.name} for dars in lesson] 

        lesson.update(is_opened=True)       

        return Response(data)
    return Response({"msg":"there is no link"})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def history(request):
    lesson = Lesson.objects.filter(user=request.user,is_opened=True).values()
    return Response(lesson,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def unstarted_lesson(request):
    lesson = Lesson.objects.filter(user=request.user,is_opened=False).values()
    return Response(lesson,status=status.HTTP_200_OK)



