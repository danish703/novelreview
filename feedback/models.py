from django.db import models

# Create your models here.

class Feedback(models.Model):
    first_name = models.TextField()
    feedback = models.TextField()

    def __str__(self):
        return self.feedback

