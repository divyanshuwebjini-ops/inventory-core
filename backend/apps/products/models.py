from django.db import models

from apps.shared.models import BaseModel, SoftDeleteModel
from apps.organizations.models import Company


class Category(BaseModel, SoftDeleteModel):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    name = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "categories"
        unique_together = ("company", "name")

    def __str__(self):
        return self.name


class Brand(BaseModel, SoftDeleteModel):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="brands",
    )

    name = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "brands"
        unique_together = ("company", "name")

    def __str__(self):
        return self.name


class Unit(BaseModel):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="units",
    )

    name = models.CharField(
        max_length=100,
    )

    short_name = models.CharField(
        max_length=20,
    )

    class Meta:
        db_table = "units"
        unique_together = ("company", "name")

    def __str__(self):
        return self.name


class Tax(BaseModel):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="taxes",
    )

    name = models.CharField(
        max_length=100,
    )

    rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    cgst = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    sgst = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    igst = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    hsn_code = models.CharField(
        max_length=20,
        blank=True,
    )

    class Meta:
        db_table = "taxes"

    def __str__(self):
        return self.name


class Product(BaseModel, SoftDeleteModel):

    GOODS = "GOODS"
    SERVICE = "SERVICE"

    PRODUCT_TYPES = [
        (GOODS, "Goods"),
        (SERVICE, "Service"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="products",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
        related_name="products",
    )

    tax = models.ForeignKey(
        Tax,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    name = models.CharField(
        max_length=255,
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
    )

    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPES,
        default=GOODS,
    )

    description = models.TextField(
        blank=True,
    )

    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    minimum_selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    reorder_level = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    track_inventory = models.BooleanField(
        default=True,
    )

    allow_negative_stock = models.BooleanField(
        default=False,
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "products"
        ordering = ["name"]
        unique_together = (
            "company",
            "name",
        )

    def __str__(self):
        return self.name