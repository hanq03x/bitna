from django.db import models
from core import models as core_models


class Post(core_models.TimeStampedModel):
    
    """ Post Model Definition """
    
    title = models.CharField(max_length=50)
    contents = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    