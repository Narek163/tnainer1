from distutils.log import debug
from email.policy import default
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Category(models.Model):
    name = models.CharField('Categoria anun', max_length=30)
    img = models.ImageField('Categoria nkar',upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Shoose(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_shose')
    name = models.CharField('Shose name',max_length=30)
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shoose'
        verbose_name_plural = 'Shooses'

class Brend(models.Model):
    shoose = models.ForeignKey(Shoose,on_delete=models.CASCADE,related_name='shoose_name')
    name = models.CharField('Brend name',max_length=30)
    img = models.ImageField('Brendi nkar',upload_to='media')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Brend'
        verbose_name_plural = 'Brends'