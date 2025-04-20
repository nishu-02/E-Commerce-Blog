from django.db import models

# Create your models here.
class Product(models.Model): # Product is the name of the table
    product_id = models.AutoField(primary_key=True) # AutoField is an auto-incrementing integer field
    product_name = models.CharField(max_length=60)
    category = models.CharField(max_length=30, default="") # max_length is the maximum length of the field
    subcategory = models.CharField(max_length=40, default="") # subcategory is the name of the field
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="description")
    pub_date = models.DateField()
    image = models.ImageField(upload_to='Core/images', default="") # upload_to is the path where the image will be stored   

    def __str__(self):
        return self.product_name # so when the whole list is displayed here we will choose what to show in the list (previously it was showing the object name)
     
class Contact(models.Model):
    msd_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    emaik = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    desc = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Order(models.Model):
    orders_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now=True) # auto_now is used to set the field to now every time the object is saved

    def __str__(self):
        return self.update_desc[0:7] + "..." # so this will return the first 7 characters of the update_desc