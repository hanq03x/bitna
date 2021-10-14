from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review Model Definition """

    review = models.TextField()
    beauty = models.IntegerField()
    size = models.IntegerField()
    color = models.IntegerField()
    finish = models.IntegerField()
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
    
    rating_average.short_description
