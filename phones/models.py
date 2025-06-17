from django.db import models
from django.db.models import SlugField
from django.utils.text import slugify


class Phone(models.Model):
    # name, price, image, release_date, lte_exists и slug
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug: SlugField = models.SlugField(max_length=1000, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)