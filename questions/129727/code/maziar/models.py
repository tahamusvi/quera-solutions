from django.db import models
from account.models import User



class Category(models.Model):
    title=models.CharField(max_length=50)
    status=models.BooleanField(default=True)

class Article(models.Model):
    STATUS_CHOICES = [
        ('d','draft'),
        ('p','publish')
    ]
    author = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='userrr')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    stauts=models.CharField(max_length=1,choices=STATUS_CHOICES,default='d')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated = self.published
        super(Article, self).save(*args, **kwargs)
    
   