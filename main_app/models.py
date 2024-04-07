from django.db import models
from datetime import date
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

MEALS = (
   ('B', 'Breakfast'),
   ('L', 'Lunch'),
   ('D', 'Dinner')
)

class Specie(models.Model):
   name = models.CharField(max_length=100)
   habitat = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Bird(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()
    species = models.ManyToManyField(Specie)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return self.name
    
    def fed_for_today(self):
     return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    
class Feeding(models.Model):
   date = models.DateField('Feeding Date')
   meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
   bird_id = models.ForeignKey(Bird, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"
   
   class Meta:
      ordering = ['-date']