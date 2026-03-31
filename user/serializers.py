from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.authentication import authenticate
User = get_user_model()

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True,style={"input_type": "password"})
    class Meta:
        model = User
        fields = ["username","password"]
    def validate_username(self, data):
        if not data[0].istitle():
            raise serializers.ValidationError("username must be capitalize")
        return data
        
    def create(self, validated_data):
        # username = validated_data["username"]
        # password = validated_data["password"]

        user = User.objects.create_user(**validated_data)
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            username = data["username"],
            password=data["password"],
        )
        if not user:
            raise serializers.ValidationError("something is error")
        data["user"]=user
        return data