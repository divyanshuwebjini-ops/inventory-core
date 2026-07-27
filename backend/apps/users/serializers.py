from rest_framework import serializers

from .models import User


class InviteUserSerializer(serializers.Serializer):

    first_name = serializers.CharField()

    last_name = serializers.CharField(required=False)

    email = serializers.EmailField()

    phone = serializers.CharField(required=False)

    role_id = serializers.UUIDField()