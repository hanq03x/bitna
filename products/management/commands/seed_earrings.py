import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from products import models as product_models


class Command(BaseCommand):
    help = "This command creates earrings"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=5, type=int, help="How many earrings you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        stones = product_models.Stone.objects.all()
        materials = product_models.Material.objects.all()
        seeder.add_entity(
            product_models.Earring,
            number,
            {
                "name": lambda x: seeder.faker.name(),
                "weight": lambda x: round(random.uniform(0.1, 10), 1),
                "stone": lambda x: random.choice(stones),
                "material": lambda x: random.choice(materials),
            },
        )
        
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            earring = product_models.Earring.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                product_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    product=earring,
                    file=f"earring_photos/{random.randint(1, 31)}.webp",
                )
        
        self.stdout.write(self.style.SUCCESS(f"{number} earrings created!"))