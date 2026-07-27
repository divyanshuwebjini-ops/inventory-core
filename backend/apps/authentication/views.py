from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, CurrentUserSerializer
from .services import RegistrationService
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAuthenticatedUser


class RegisterAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        result = RegistrationService.register(
            serializer.validated_data
        )

        return Response(
            {
                "message": "Registration successful.",
                "access": result["access"],
                "refresh": result["refresh"],
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        result = RegistrationService.login(
            serializer.validated_data
        )

        return Response(
            {
                "message": "Login successful",

                "access": result["access"],

                "refresh": result["refresh"],
            }
        )
    

class MeAPIView(APIView):

    permission_classes = [
        IsAuthenticatedUser,
    ]

    def get(self, request):

        serializer = CurrentUserSerializer(
            request.user
        )

        return Response(serializer.data)