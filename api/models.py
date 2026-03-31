from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
    

class Lesson(models.Model):
    name=models.CharField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="lessons")
    link = models.URLField()
    start_time = models.DateTimeField()
    is_opened = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    class WeekDay(models.TextChoices):
        Monday = "Monday","Monday"
        Thuesday = "Thuesday", "Thuesday"
        Wensday = "Wednesday", "Wednesday"
        Thursday = "Thursday", "Thursday"
        Friday = "Friday","Friday"
        Saturday = "Saturday","Saturday"
        Sunday = "Sunday", "Sunday"
        

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    week_day = models.CharField(choices=WeekDay)
    start_time = models.TimeField()
    end_time = models.TimeField()


    def __str__(self):
        return self.week_day
    