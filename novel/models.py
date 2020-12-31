from django.db import models
from django.db.models import Sum,Count

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Novel(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='novelimage/')
    author=models.CharField(max_length=100)
    release_year = models.CharField(max_length=4)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def averageRate(self):
        from comment.models import Comment
        sums = Comment.objects.filter(novel=self).aggregate(Sum('rating'))
        c = Comment.objects.filter(novel=self).aggregate(Count('rating'))
        if sums['rating__sum'] == None:
            avg = 0;
        else:
            avg = sums['rating__sum'] / c['rating__count']
        return round(avg,2)

    @property
    def countRate(self):
        from comment.models import Comment
        cr = Comment.objects.filter(novel=self).aggregate(Count('rating'))
        counted = cr['rating__count']
        return counted

    @property
    def count1(self):
        from comment.models import Comment
        one = Comment.objects.filter(novel=self,rating='1').aggregate(Count('rating'))
        ones = one['rating__count']
        return ones

    @property
    def count2(self):
        from comment.models import Comment
        one = Comment.objects.filter(novel=self, rating='2').aggregate(Count('rating'))
        ones = one['rating__count']
        return ones

    @property
    def count3(self):
        from comment.models import Comment
        one = Comment.objects.filter(novel=self, rating='3').aggregate(Count('rating'))
        ones = one['rating__count']
        return ones

    @property
    def count4(self):
        from comment.models import Comment
        one = Comment.objects.filter(novel=self, rating='4').aggregate(Count('rating'))
        ones = one['rating__count']
        return ones

    @property
    def count5(self):
        from comment.models import Comment
        one = Comment.objects.filter(novel=self, rating='5').aggregate(Count('rating'))
        ones = one['rating__count']
        return ones




