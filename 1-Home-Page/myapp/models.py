from django.utils.text import slugify 
from django.db import models
from django.urls import reverse

class Product_Name(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='') 
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product_Name, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
