from django.db import models

class Writer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

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
    isbn = models.IntegerField()
    synopsis = models.TextField()
    page = models.IntegerField()
    cover = models.ImageField()
    date = models.DateField()