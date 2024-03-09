from typing import Iterable
from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify

# Create your models here.
class ObjectModel( models.Model ):
    title = models.CharField( max_length = 64, blank = False )
    description = models.CharField( max_length = 128, blank = False )
    timestamp = models.DateTimeField( auto_now_add = True, blank = False )
    slug = models.SlugField( max_length = 100, blank = True, unique = True )

    def save(self, **kwargs) -> None:
        self.slug = slugify(self.title)R
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse_lazy("app:list") + f"#object-{self.slug}"
    
    def get_update_url(self):
        return reverse("app:edit", kwargs = {"slug": self.slug})

    def __str__(self):
        return self.title

