from django.db import models
from django.contrib.auth.models import User
from novel.models import Novel
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Sum,Count
# Create your models here.
CHOICES = (('positive','Positive'),('negative','Negative'))
class Comment(models.Model):
    comment_message = models.TextField()
    novel = models.ForeignKey(Novel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    status = models.CharField(choices=CHOICES, max_length=20, default='positive')

    class Meta:
        unique_together=('novel','user')

    def __str__(self):
        return self.comment_message


