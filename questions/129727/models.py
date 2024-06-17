from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Category(models.Model):
    title=models.CharField(max_length=50)
    status=models.BooleanField(default=True)

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft','d'),
        ('publish','p')
    ]
    author = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='user')
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
    
    """

    and suddely i had this error!
     author = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='user'
     is it gonna solve it?
    
    account.User.groups: (fields.E304) Reverse accessor for 'account.User.groups' clashes with reverse accessor for 'blog.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'account.User.groups' or 'blog.User.groups'.
account.User.user_permissions: (fields.E304) Reverse accessor for 'account.User.user_permissions' clashes with reverse accessor for 'blog.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'account.User.user_permissions' or 'blog.User.user_permissions'.
blog.User.groups: (fields.E304) Reverse accessor for 'blog.User.groups' clashes with reverse accessor for 'account.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'blog.User.groups' or 'account.User.groups'.
blog.User.user_permissions: (fields.E304) Reverse accessor for 'blog.User.user_permissions' clashes with reverse accessor for 'account.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'blog.User.user_permissions' or 'account.User.user_permissions'.
    
    """