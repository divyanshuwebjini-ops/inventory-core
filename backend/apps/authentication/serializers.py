from django.contrib.auth import authenticate
from rest_framework import serializers
from apps.users.models import User


class RegisterSerializer(serializers.Serializer):

    company_name = serializers.CharField(max_length=255)
    subdomain = serializers.SlugField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField()
    phone = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)
    gst_number = serializers.CharField(required=False)
    def validate_email(self, value):

        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value.lower()



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):
        user = User.objects.filter(
            email=attrs["email"].lower()
        ).first()

        if not user:
            raise serializers.ValidationError(
                "Invalid Email or Password."
            )

        if not user.check_password(
            attrs["password"]
        ):
            raise serializers.ValidationError(
                "Invalid Email or Password."
            )

        attrs["user"] = user

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(min_length=8)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField(min_length=8)


class CurrentUserSerializer(serializers.ModelSerializer):

    full_name = serializers.ReadOnlyField()

    company = serializers.SerializerMethodField()

    roles = serializers.SerializerMethodField()

    permissions = serializers.SerializerMethodField()

    class Meta:

        model = User

        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone",
            "company",
            "roles",
            "permissions",
        )

    def get_company(self, obj):

        return {
            "id": str(obj.company.id),
            "name": obj.company.name,
            "subdomain": obj.company.subdomain,
        }

    def get_roles(self, obj):

        return [
            {
                "id": str(role.id),
                "name": role.name,
            }
            for role in obj.roles.all()
        ]

    def get_permissions(self, obj):

        permissions = set()

        for role in obj.roles.prefetch_related("permissions"):

            for permission in role.permissions.all():

                permissions.add(permission.code)

        return sorted(permissions)