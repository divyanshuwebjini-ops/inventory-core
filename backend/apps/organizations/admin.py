from django.contrib import admin

from .models import Company, Branch, Warehouse


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "subdomain",
        "email",
        "phone",
        "gst_number",
        "is_active",
    )

    search_fields = (
        "name",
        "email",
        "gst_number",
    )


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "company",
        "code",
        "city",
        "is_head_office",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "company",
        "is_head_office",
    )


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "branch",
        "company",
        "code",
        "is_default",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "company",
        "branch",
    )