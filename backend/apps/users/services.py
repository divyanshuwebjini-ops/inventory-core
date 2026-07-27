from django.shortcuts import get_object_or_404

from .models import User, Role


class UserService:

    @staticmethod
    def invite(company, validated_data):

        role = get_object_or_404(
            Role,
            id=validated_data["role_id"],
            company=company,
        )

        user = User.objects.create(
            company=company,
            first_name=validated_data["first_name"],
            last_name=validated_data.get("last_name", ""),
            email=validated_data["email"],
            phone=validated_data.get("phone", ""),
            is_invited=True,
        )

        user.roles.add(role)

        return user