from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Lesson,Schedule

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ["user"]

class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
    
    def validate(self, value):
        if not value["start_time"]< value["end_time"]:
            raise serializers.ValidationError("end_time must be greter than start_time")
        return value
    def validate(self,value):
        if not (value["end_time"]-value["start_time"]<80):
            raise serializers.ValidationError("time must be at least 80 minutes")
        return value