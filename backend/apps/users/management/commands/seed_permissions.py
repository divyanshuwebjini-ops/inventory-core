from django.core.management.base import BaseCommand

from apps.users.models import Permission


PERMISSIONS = [

    # Products
    ("Products", "products.view"),
    ("Products", "products.create"),
    ("Products", "products.update"),
    ("Products", "products.delete"),

    # Inventory
    ("Inventory", "inventory.view"),
    ("Inventory", "inventory.adjust"),
    ("Inventory", "inventory.transfer"),

    # Customers
    ("Customers", "customers.view"),
    ("Customers", "customers.create"),
    ("Customers", "customers.update"),
    ("Customers", "customers.delete"),

    # Suppliers
    ("Suppliers", "suppliers.view"),
    ("Suppliers", "suppliers.create"),
    ("Suppliers", "suppliers.update"),
    ("Suppliers", "suppliers.delete"),

    # Purchases
    ("Purchases", "purchases.view"),
    ("Purchases", "purchases.create"),
    ("Purchases", "purchases.update"),
    ("Purchases", "purchases.delete"),

    # Sales
    ("Sales", "sales.view"),
    ("Sales", "sales.create"),
    ("Sales", "sales.update"),
    ("Sales", "sales.delete"),

    # Invoices
    ("Invoices", "invoices.view"),
    ("Invoices", "invoices.create"),
    ("Invoices", "invoices.cancel"),
    ("Invoices", "invoices.print"),

    # Payments
    ("Payments", "payments.view"),
    ("Payments", "payments.create"),
    ("Payments", "payments.delete"),

    # Reports
    ("Reports", "reports.view"),

    # Users
    ("Users", "users.view"),
    ("Users", "users.create"),
    ("Users", "users.update"),
    ("Users", "users.delete"),

    # Roles
    ("Roles", "roles.view"),
    ("Roles", "roles.create"),
    ("Roles", "roles.update"),
    ("Roles", "roles.delete"),

    # Company
    ("Company", "company.view"),
    ("Company", "company.update"),

    # Settings
    ("Settings", "settings.view"),
    ("Settings", "settings.update"),
]


class Command(BaseCommand):

    help = "Seed default permissions"

    def handle(self, *args, **kwargs):

        created = 0

        for module, code in PERMISSIONS:

            permission, is_created = Permission.objects.get_or_create(

                code=code,

                defaults={

                    "name": code.replace(".", " ").title(),

                    "module": module,

                    "description": "",

                },

            )

            if is_created:
                created += 1

        self.stdout.write(

            self.style.SUCCESS(

                f"{created} permissions created."

            )

        )