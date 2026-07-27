from django.utils.text import slugify

from apps.organizations.models import Company


def generate_unique_subdomain(company_name):
    """
    Generates a unique company subdomain.
    """

    base = slugify(company_name)

    slug = base

    counter = 1

    while Company.objects.filter(subdomain=slug).exists():

        counter += 1

        slug = f"{base}-{counter}"

    return slug