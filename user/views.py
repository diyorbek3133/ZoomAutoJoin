from django.shortcuts import render
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        # raise Exception(request.data)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response({
            "username":user.username,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
            },status=status.HTTP_200_OK
        )
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)