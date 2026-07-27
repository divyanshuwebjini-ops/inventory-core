from django.db import models

from apps.shared.models import BaseModel, SoftDeleteModel


class Company(BaseModel, SoftDeleteModel):
    """
    Company/Tenant
    """

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    legal_name = models.CharField(
        max_length=255,
        blank=True,
    )

    subdomain = models.SlugField(
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    gst_number = models.CharField(
        max_length=15,
        blank=True,
    )

    pan_number = models.CharField(
        max_length=10,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    state = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    pincode = models.CharField(
        max_length=10,
        blank=True,
    )

    logo = models.ImageField(
        upload_to="companies/logos/",
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
    )

    financial_year_start = models.DateField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "companies"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Branch(BaseModel, SoftDeleteModel):
    """
    Company Branch
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="branches",
    )

    name = models.CharField(
        max_length=150,
    )

    code = models.CharField(
        max_length=20,
    )

    gst_number = models.CharField(
        max_length=15,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    state = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    pincode = models.CharField(
        max_length=10,
        blank=True,
    )

    is_head_office = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "branches"
        ordering = ["name"]
        unique_together = ("company", "code")

    def __str__(self):
        return f"{self.company.name} - {self.name}"
    


class Warehouse(BaseModel, SoftDeleteModel):
    """
    Company Warehouse
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="warehouses",
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="warehouses",
    )

    name = models.CharField(
        max_length=150,
    )

    code = models.CharField(
        max_length=20,
    )

    address = models.TextField(
        blank=True,
    )

    manager_name = models.CharField(
        max_length=150,
        blank=True,
    )

    manager_phone = models.CharField(
        max_length=20,
        blank=True,
    )

    is_default = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "warehouses"
        ordering = ["name"]
        unique_together = (
            "company",
            "code",
        )

    def __str__(self):
        return f"{self.branch.name} - {self.name}"
    


class FinancialYear(BaseModel):
    """
    Financial year for a company.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="financial_years",
    )

    name = models.CharField(
        max_length=20,
    )

    start_date = models.DateField()

    end_date = models.DateField()

    is_current = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "financial_years"
        ordering = ["-start_date"]

    def __str__(self):
        return self.name


class CompanySetting(BaseModel):
    """
    Company-wide ERP settings.
    """

    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name="settings",
    )

    currency = models.CharField(
        max_length=10,
        default="INR",
    )

    timezone = models.CharField(
        max_length=100,
        default="Asia/Kolkata",
    )

    date_format = models.CharField(
        max_length=20,
        default="DD/MM/YYYY",
    )

    enable_gst = models.BooleanField(
        default=True,
    )

    enable_barcode = models.BooleanField(
        default=True,
    )

    enable_multi_warehouse = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "company_settings"

    def __str__(self):
        return f"{self.company.name} Settings"