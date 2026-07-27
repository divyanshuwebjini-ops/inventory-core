# from django.db import models

# from apps.shared.models import BaseModel
# from apps.organizations.models import Company, Branch
# from apps.customers.models import Customer


# class Sale(BaseModel):

#     DRAFT = "DRAFT"
#     CONFIRMED = "CONFIRMED"
#     CANCELLED = "CANCELLED"

#     STATUS_CHOICES = [
#         (DRAFT, "Draft"),
#         (CONFIRMED, "Confirmed"),
#         (CANCELLED, "Cancelled"),
#     ]

#     company = models.ForeignKey(
#         Company,
#         on_delete=models.CASCADE,
#         related_name="sales",
#     )

#     branch = models.ForeignKey(
#         Branch,
#         on_delete=models.CASCADE,
#         related_name="sales",
#     )

#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.PROTECT,
#         related_name="sales",
#     )

#     invoice_number = models.CharField(
#         max_length=50,
#         unique=True,
#     )

#     invoice_date = models.DateField()

#     subtotal = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#         default=0,
#     )

#     discount = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#         default=0,
#     )

#     tax_amount = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#         default=0,
#     )

#     grand_total = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#         default=0,
#     )

#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default=DRAFT,
#     )

#     notes = models.TextField(
#         blank=True,
#     )

#     class Meta:
#         db_table = "sales"
#         ordering = ["-invoice_date"]

#     def __str__(self):
#         return self.invoice_number
    


# from apps.products.models import Product
# from apps.organizations.models import Warehouse


# class SaleItem(BaseModel):

#     sale = models.ForeignKey(
#         Sale,
#         on_delete=models.CASCADE,
#         related_name="items",
#     )

#     warehouse = models.ForeignKey(
#         Warehouse,
#         on_delete=models.PROTECT,
#     )

#     product = models.ForeignKey(
#         Product,
#         on_delete=models.PROTECT,
#     )

#     quantity = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#     )

#     unit_price = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#     )

#     discount = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#         default=0,
#     )

#     tax_percentage = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         default=0,
#     )

#     tax_amount = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#         default=0,
#     )

#     total = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#     )

#     class Meta:
#         db_table = "sale_items"

#     def __str__(self):
#         return self.product.name
    


# class SalePayment(BaseModel):

#     CASH = "CASH"
#     CARD = "CARD"
#     UPI = "UPI"
#     BANK = "BANK"

#     PAYMENT_METHODS = [
#         (CASH, "Cash"),
#         (CARD, "Card"),
#         (UPI, "UPI"),
#         (BANK, "Bank Transfer"),
#     ]

#     sale = models.ForeignKey(
#         Sale,
#         on_delete=models.CASCADE,
#         related_name="payments",
#     )

#     amount = models.DecimalField(
#         max_digits=15,
#         decimal_places=2,
#     )

#     payment_method = models.CharField(
#         max_length=20,
#         choices=PAYMENT_METHODS,
#     )

#     reference_number = models.CharField(
#         max_length=100,
#         blank=True,
#     )

#     payment_date = models.DateField()

#     class Meta:
#         db_table = "sale_payments"

#     def __str__(self):
#         return f"{self.sale.invoice_number} - {self.amount}"