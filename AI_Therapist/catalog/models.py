from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User

class Doctor(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    clinic_address = models.CharField(max_length=200)
    
    mobile_number = models.CharField(max_length=200)
   

    class Meta:
        ordering=['-name']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for a particular doctor."""
        return reverse('doctor-detail', args=[str(self.id)])
from datetime import date
class Calendar(models.Model):
    MOODS=(
        ('d','Depressed'),
        ('a','Angry'),
        ('w','Workload'),
        ('s','Sad'),
        ('r','Relationship Problems'),
        ('t','Tensed About Past')
        )
    mood=models.CharField(
        max_length=1,
        choices=MOODS,
        
    )
    mood_date=models.DateField(null=True, blank=True)
    yachak = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    mood_time=models.TimeField(auto_now=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.mood
    
    def get_absolute_url(self):
        
        return reverse('mood-detail', args=[str(self.id)])
    def mood_verbose(self):
        return dict(Calendar.MOODS)[self.mood]



    
    

    