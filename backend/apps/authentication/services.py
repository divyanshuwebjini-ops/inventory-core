from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from apps.organizations.models import Company
from apps.users.models import User, Role, Permission
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class RegistrationService:

    @staticmethod
    @transaction.atomic
    def register(validated_data):

        if Company.objects.filter(
            subdomain=validated_data["subdomain"]
        ).exists():
            raise ValidationError("Subdomain already exists.")

        if User.objects.filter(
            email=validated_data["email"]
        ).exists():
            raise ValidationError("Email already exists.")

        company = Company.objects.create(
            name=validated_data["company_name"],
            legal_name=validated_data["company_name"],
            subdomain=validated_data["subdomain"],
            email=validated_data["email"],
            phone=validated_data.get("phone", ""),
            gst_number=validated_data.get("gst_number", ""),
        )

        owner = User.objects.create_user(
            company=company,
            first_name=validated_data["first_name"],
            last_name=validated_data.get("last_name", ""),
            email=validated_data["email"],
            phone=validated_data.get("phone", ""),
            password=validated_data["password"],
            is_staff=True,
        )

        admin_role = RegistrationService.create_default_roles(company)

        owner.roles.add(admin_role)

        refresh = RefreshToken.for_user(owner)

        return {
            "user": owner,
            "company": company,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

    @staticmethod
    def create_default_roles(company):

        admin = Role.objects.create(
            company=company,
            name="Administrator",
            description="Full system access",
        )

        manager = Role.objects.create(
            company=company,
            name="Manager",
            description="Department manager",
        )

        accountant = Role.objects.create(
            company=company,
            name="Accountant",
            description="Accounts team",
        )

        staff = Role.objects.create(
            company=company,
            name="Staff",
            description="Normal employee",
        )

        permissions = Permission.objects.all()

        admin.permissions.set(permissions)

        return admin
    

    
    @staticmethod
    def login(validated_data):

        user = authenticate(
            email=validated_data["email"],
            password=validated_data["password"],
        )

        if not user:
            raise AuthenticationFailed(
                "Invalid email or password."
            )

        refresh = RefreshToken.for_user(user)

        return {
            "user": user,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }