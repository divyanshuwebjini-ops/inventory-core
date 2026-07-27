from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import InviteUserSerializer
from .services import UserService


class InviteUserAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):

        serializer = InviteUserSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = UserService.invite(
            request.user.company,
            serializer.validated_data,
        )

        return Response(
            {
                "message": "User invited.",
                "invite_token": user.invite_token,
            }
        )