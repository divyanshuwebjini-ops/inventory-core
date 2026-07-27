from django.db import models

from apps.shared.models import BaseModel
from apps.organizations.models import Company, Branch, Warehouse
from apps.products.models import Product


class Inventory(BaseModel):
    """
    Current stock of a product in a warehouse.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="inventories",
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="inventories",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="inventories",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="inventories",
    )

    quantity = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )

    reserved_quantity = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )

    average_cost = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )

    class Meta:
        db_table = "inventories"

        unique_together = (
            "warehouse",
            "product",
        )

    def __str__(self):
        return f"{self.product.name} ({self.warehouse.name})"
    


class InventoryTransaction(BaseModel):

    PURCHASE = "PURCHASE"
    SALE = "SALE"
    RETURN = "RETURN"
    ADJUSTMENT = "ADJUSTMENT"
    TRANSFER = "TRANSFER"

    TRANSACTION_TYPES = [
        (PURCHASE, "Purchase"),
        (SALE, "Sale"),
        (RETURN, "Return"),
        (ADJUSTMENT, "Adjustment"),
        (TRANSFER, "Transfer"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    transaction_type = models.CharField(
        max_length=30,
        choices=TRANSACTION_TYPES,
    )

    quantity = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    unit_cost = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )

    reference = models.CharField(
        max_length=100,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "inventory_transactions"

    def __str__(self):
        return self.transaction_type