from django.core.management.base import BaseCommand
from products.models import Stone

class Command(BaseCommand):

    help = "This command creates stones"

    def handle(self, *args, **options):
        stones = [
            "가넷",
            "자수정",
            "아쿠아마린",
            "다이아몬드",
            "에메랄드",
            "진주",
            "루비",
            "페리도트",
            "사파이어",
            "오팔",
            "토파즈",
            "터키석"
            "호박",
            "큐빅",
        ]
        for s in stones:
            Stone.objects.create(name=s)
        self.stdout.write(self.style.SUCCESS(f"{len(stones)} Stones Created"))