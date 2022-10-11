from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import Http404
from .models import CustomUser
from rest_framework import viewsets
from .serializers import (
    LoginCustomUserSerializer,
    CustomUserSerializer,
    UpdateUserSerializer,
    ChangePasswordSerializer,
)


class LoginCustomUserApi(APIView):
    def post(self, request):
        serializer = LoginCustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise ValidationError({"detail": "Incorrect username, or password"})

        return Response(
            {
                "user": CustomUserSerializer(instance=user).data,
            },
            status=status.HTTP_200_OK,
        )


class CustomUserView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.all().prefetch_related('orders')

    def get_permission_classes(self):
        permission_classes = [permissions.AllowAny]
        if self.action == ["destroy", "list"]:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = CustomUserSerializer
        if self.action == "retrieve":
            serializer_class = UpdateUserSerializer
        return serializer_class

    def retrieve(self, *args, **kwargs):
        if self.kwargs['pk'] == 'me':
            return Response(CustomUserSerializer(self.request.user).data)
        else:
            return Response(CustomUserSerializer(CustomUser.objects.get(pk=self.kwargs['pk'])).data)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all().prefetch_related('orders')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class CustomUserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all().prefetch_related('orders')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateUserSerializer
