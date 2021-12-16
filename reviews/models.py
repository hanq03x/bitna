from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review Model Definition """

    review = models.TextField()
    beauty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    color = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    finish = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey("users.User", related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.user}"

    def rating_average(self):
        avg = (
            self.beauty
            + self.size
            + self.color
            + self.finish
        ) / 4
        return round(avg, 1)
    
    rating_average.short_description = "Avg."

    class Meta:
        ordering = ("-created",)
