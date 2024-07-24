from django.shortcuts import render
from account.serializer import SignUpSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    if serializer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],  # Use email as username
                email=data['email'],
                password=make_password(data['password'])  # Ensure password is hashed
            )
            return Response(
                {'message': 'User created successfully'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'message': 'User already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userInfo(request):
    user_serializer = UserSerializer(request.user)
    return Response({'user': user_serializer.data})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserInfo(request):
    user = request.user
    user.first_name = request.data['first_name']
    user.last_name = request.data['last_name']
    user.username = request.data['username']
    user.save()
    user_serializer = UserSerializer(request.user)
    return Response({'user': user_serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request):
    user = request.user
    user.delete()
    return Response({'msg': 'user deleted'})