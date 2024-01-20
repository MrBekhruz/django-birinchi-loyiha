from django.db import models
from django.urls import reverse

regions = [
    ('Toshkent','Toshkent'),
    ('Qoraqalpog\iston Respublikasi','Qoraqalpog\iston Respublikasi'),
    ('Farg\ona','Farg\ona'),
    ('Namangan','Namangan'),
    ('Andijon','Andijon'),
    ('Jizzax','Jizzax'),
    ('Sirdaryo','Sirdaryo'),
    ('Samarqand','Samarqand'),
    ('Buxoro','Buxoro'),
    ('Qashqadaryo','Qashqadaryo'),
    ('Surxandaryo','Surxandaryo'),
    ('Navoiy','Navoiy'),
    ('Xorazm viloyati','Xorazm viloyati'),
]


class Bulim(models.Model):
    title = models.CharField(max_length = 255)

    def __str__(self):
        return self.title
    

class BulimData(models.Model):
    post_category = models.ForeignKey(Bulim, on_delete=models.CASCADE ) #post categoryga foregn key orqali post ga ulanyapti on_delete =models.cascade bu uzgarmas qonun yozish shart
    #post esa bevosita views faylga ulanyapti
    post_title = models.CharField(max_length=255)
    fr_content = models.TextField()
    post_image = models.TextField()
    post_hashtag = models.CharField(max_length = 255)
    post_date = models.DateTimeField(auto_now = False)

    def get_absolute_url(self):
        return reverse('bulim',kwargs={'pk':self.pk})

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name



class Post(models.Model):
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE ) #post categoryga foregn key orqali post ga ulanyapti on_delete =models.cascade bu uzgarmas qonun yozish shart
    #post esa bevosita views faylga ulanyapti
    post_title = models.CharField(max_length=255)
    fr_content = models.TextField()
    post_image = models.TextField()
    post_hashtag = models.CharField(max_length = 255)
    post_date = models.DateTimeField(auto_now = False)

    def __str__(self):
        return self.post_hashtag  




class PostRegion(models.Model):
    post_regions = models.CharField(max_length = 255,choices = regions)
    post_title = models.CharField(max_length = 255)
    fr_content = models.TextField()
    post_image = models.TextField()
    post_hashtag = models.CharField(max_length = 255)
    post_date = models.DateTimeField(auto_now = False) # kirgan vaqtdan boshlab registratsiya buladi auto_now = False orqali

    def __str__(self):
        return self.post_title  
    



