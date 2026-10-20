from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User


class CalorieProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name
    
class FoodEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    item_name = models.CharField(max_length=100)
    calorie_consumed = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name