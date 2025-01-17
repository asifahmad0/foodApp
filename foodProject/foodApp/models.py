from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.

class itemsList(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name

class items(models.Model):
    item_name=models.CharField(max_length=20)
    description= models.TextField(blank=False)
    img= models.ImageField(upload_to='items/',)
    price = models.BigIntegerField()
    category= models.ForeignKey(itemsList, on_delete=models.CASCADE, related_name='Category')

    def __str__(self):
        return self.item_name


class book_table(models.Model):
    user_name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email= models.EmailField()
    persion = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user_name


class Review(models.Model):
    user_name= models.CharField(max_length=100)
    feedbacks= models.TextField(blank=False)
    rating= models.IntegerField()
    img= models.ImageField(upload_to='items/', default='items/client1.jpg')

    def __str__(self):
        return self.user_name

