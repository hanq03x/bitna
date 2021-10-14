from django.db import models
from core import models as core_models


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
    file = models.ImageField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Product(core_models.TimeStampedModel):
    """ Product Model Definition """

    name = models.CharField(max_length=140)
    material = models.ForeignKey("Material", on_delete=models.SET_NULL, null=True)
    weight = models.FloatField(null=True)

    def __str__(self):
        return self.name


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
