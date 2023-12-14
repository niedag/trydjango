from django.db import models

# Create your models here.
class Product(models.Model): #We use model fields in order to map to the database
    title       = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = False) # BLANK has to do with how the field is rendered
    price       = models.DecimalField(max_digits = 10000, decimal_places=2)
    summary     = models.TextField(blank = False, null = False) # null has to do with the database
    featured    = models.BooleanField(default = False) # null = True, default = true
    email       = models.EmailField(max_length=120, default = False)
    # if blank is False: it will render as required
    # if null True/False, means whether it can be empty/null in the database

    def get_absolute_url(self):
        return reverse("product-detail", kwargs = {"my_id": self.id})