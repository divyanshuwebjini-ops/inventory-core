from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
import uuid
from apps.shared.models import BaseModel
from apps.organizations.models import Company
from .managers import UserManager


class Permission(BaseModel):
    """
    System permissions.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    module = models.CharField(max_length=100)

    class Meta:
        db_table = "permissions"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Role(BaseModel):
    """
    Company specific roles.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="roles",
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="roles",
    )

    is_system = models.BooleanField(
        default=False,
    )

    color = models.CharField(
        max_length=20,
        default="#4F46E5",
    )

    priority = models.PositiveSmallIntegerField(
        default=100,
    )

    class Meta:
        db_table = "roles"
        ordering = ["priority", "name"]
        unique_together = ("company", "name")

    def __str__(self):
        return f"{self.company.name} - {self.name}"

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    Custom User Model.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="users",
    )

    roles = models.ManyToManyField(
        Role,
        blank=True,
        related_name="users",
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    is_owner = models.BooleanField(
        default=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    last_login_ip = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    last_activity = models.DateTimeField(
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to="users/profile/",
        blank=True,
        null=True,
    )

    is_system = models.BooleanField(
        default=False,
    )

    color = models.CharField(
        max_length=20,
        default="#4F46E5",
    )

    invite_token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        null=True,
        blank=True,
    )

    is_email_verified = models.BooleanField(
        default=False,
    )

    is_invited = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        ordering = ["first_name"]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()