from django.db import models
from django.urls import reverse
from core import models as core_models
from reviews.models import Review


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Material(AbstractItem):
    """ Material Model Definition """

    class Meta:
        verbose_name_plural = "Materials"


class Stone(AbstractItem):
    """ Stone Model Definition """
    
    class Meta:
        verbose_name_plural = "Stones"


class Photo(core_models.TimeStampedModel):
    
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    product = models.ForeignKey("Product", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Product(core_models.TimeStampedModel):
    """ Product Model Definition """

    name = models.CharField(max_length=140)
    weight = models.FloatField(null=True)
    material = models.ForeignKey("Material", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})
    
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return round(all_ratings / len(all_reviews), 1) if len(all_reviews) else "0"

    def first_photo(self):
        photo, = self.photos.all()[:1]
        return photo.file.url

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos


class Ring(Product):
    """ Ring Model Definition """

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_COUPLE = 'couple'
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_COUPLE, "Couple"),
    )
    stone = models.ForeignKey("Stone", on_delete=models.SET_NULL, null=True)
    size = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=140)


class Earring(Product):
    """ Earring Model Definition """
    
    stone = models.ForeignKey("Stone", on_delete=models.SET_NULL, null=True)


class Necklace(Product):
    """ Necklace Model Definition """

    size = models.IntegerField()
    stone = models.ForeignKey("Stone", on_delete=models.SET_NULL, null=True)


class Bracelet(Product):
    """ Bracelet Model Definition """

    size = models.IntegerField(null=True)
