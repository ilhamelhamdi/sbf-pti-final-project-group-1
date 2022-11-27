from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

class Writer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    synopsis = models.TextField()
    page = models.IntegerField(validators=[MinValueValidator(1)])
    cover = models.ImageField(upload_to='upload')
    date = models.DateField()