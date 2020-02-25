from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, TokenSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
# class UserDetails(generics.ListCreateAPIView):
#     permissions_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
    
#     def name(request):
#         username = None
#         if request.user.is_authenticated:
#             username = request.user.username
#             return username
#         else:
#             pass

class LoginView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                "token": str(refresh.access_token)
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class RegisterUsersView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        first = request.data.get("first", "")
        last = request.data.get("last", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, first and last name, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        new_user.first_name = first
        new_user.last_name = last
        new_user.save()
        return Response(status=status.HTTP_201_CREATED)


