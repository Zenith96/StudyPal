from django.db import models
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
    task_number= models.PositiveIntegerField()
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return f"Task {self.task_number}"
    
    class Meta:
        ordering = ['-date_posted']
        verbose_name_plural = "Tasks"  




class Notes(models.Model):
    note_number = models.PositiveIntegerField()
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return f"Note {self.note_number}"
    
    class Meta:
        ordering = ['-date_posted']
        verbose_name_plural = "Notes"  

