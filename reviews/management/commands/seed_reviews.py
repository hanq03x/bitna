import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from products import models as products_models


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=20, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        products = products_models.Product.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "beauty": lambda x: random.randint(1, 5),
                "size": lambda x: random.randint(1, 5),
                "color": lambda x: random.randint(1, 5),
                "finish": lambda x: random.randint(1, 5),
                "product": lambda x: random.choice(products),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))