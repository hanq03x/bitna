from django.core.management.base import BaseCommand
from products.models import Material

class Command(BaseCommand):

    help = "This command creates materials"

    def handle(self, *args, **options):
        materials = [
            "순금(24K)",
            "골드(18K)",
            "골드(14K)",
            "핑크골드(18K)",
            "핑크골드(14K)",
            "화이트골드(18K)",
            "화이트골드(14K)",
            "실버",
            "백금",
        ]
        for m in materials:
            Material.objects.create(name=m)
        self.stdout.write(self.style.SUCCESS(f"{len(materials)} Materials Created"))