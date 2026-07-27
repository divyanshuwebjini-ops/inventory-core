import uuid

from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    """
    Adds created and updated timestamps.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """
    Soft delete support.
    """

    is_active = models.BooleanField(
        default=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class AuditModel(models.Model):
    """
    Tracks who created and last updated a record.
    Use only for business entities.
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created",
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated",
    )

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):
    """
    Base model used by all entities.
    Provides UUID + timestamps.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True