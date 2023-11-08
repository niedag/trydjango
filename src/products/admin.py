from django.contrib import admin

# A relative import: importing Product class from models.py -- relative bc admin.py and models.py are in the same directory
from .models import Product # To look at this model inside of the admin

# 10-12-23 You only need to create a migration and migrate a change if is a change to the database schema

admin.site.register(Product)
