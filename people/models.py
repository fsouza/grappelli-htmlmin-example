from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    owners = models.ManyToManyField(Person)

    def __unicode__(self):
        return self.name
