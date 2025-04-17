from django.db import models

# Create your models here.
class Product(models.Model): # Product is the name of the table
    product_id = models.AutoField(primary_key=True) # AutoField is an auto-incrementing integer field
    product_name = models.CharField(max_length=60)
    desc = models.CharField(max_length=300, default="description")
    pub_date = models.DateField()
