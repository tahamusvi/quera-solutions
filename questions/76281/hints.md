# Question 76281


**Question Title**: jitsi

**Question Link**: [jitsi](https://quera.org/problemset/76281) 

**Difficulty Level**: 🟠


## Key Points

1. **Difference is usage of User and AbstractUser**

When creating a custom user model in Django, you have two main options: inheriting from User  # __(django.contrib.auth.models.User)__ or AbstractUser __(django.contrib.auth.models.AbstractUser)__. Here's a breakdown of the differences between the two approaches:

**Extending the Built-in User Model:**

By inheriting from User, you are extending the built-in user model and can add additional fields or methods. The existing fields and behavior of User will be preserved in your custom model.
Your custom model will have all the default user fields like username, email, password, etc.
However, there are limitations when extending User. For example, you cannot modify any of the existing fields or change the model's unique constraints.

__When to use:__ 

If you only need to add a few extra fields or extend functionality without changing the fundamental structure of the user model.

__How it works:__ 

You create a one-to-one relationship with Django's default User model using a profile model.

```python
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.URLField()
```

__Pros:__

 Simple and works well if you just need to store additional information related to users.

__Cons:__ 

If you want deeper customization (e.g., changing the username field, email as the primary identifier), this approach is limited.

**Substituting the User Model with AbstractUser or AbstractBaseUser:**

__Using AbstractUser:__

__When to use:__

 When you want to customize the user model but still want to retain the basic fields and behavior of Django’s default User model (like username, password, email, etc.).

__How it works:__ 

You subclass AbstractUser and add or modify fields as needed.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField()
    website = models.URLField()
```

__Pros:__

- Inherits all the built-in functionalities of Django’s default user model.-
- Easier to set up since you don't have to define every field from scratch.
- Ideal if you only need to add a few fields or slightly modify the existing fields.

__Cons:__

 Less flexibility compared to AbstractBaseUser if you want to fully customize the user model (e.g., changing how authentication works).


__Using AbstractBaseUser:__

__When to use:__

When you need complete control over the user model and authentication mechanism (e.g., changing how users log in, fully customizing fields).

__How it works:__

 You subclass AbstractBaseUser and build the user model from scratch. You’ll need to define all fields (like username, email, etc.) and manage the authentication workflow.

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']



```
**Key Differences Between User, AbstractUser, and AbstractBaseUser:**

User: The default model provided by Django. You cannot directly customize it except by extending it with a profile model.

AbstractUser: Provides all the fields and methods of the default User model, but you can subclass it to add or change fields.

AbstractBaseUser: The most flexible option, allowing you to build a completely custom user model from the ground up. You have to define all fields and authentication logic manually.




2. **get_or_create**

The get_or_create method in Django is a built-in method provided by Django's Model Managers. It's a combination of a get and a create method that allows you to retrieve an object from the database based on certain parameters, or create a new one if it doesn't exist yet.
The method signature for get_or_create looks like this:
```python
get_or_create(defaults=None, **kwargs)
```
Here's what it does:
- Filtering: It first tries to retrieve an object from the database using the keyword arguments (**kwargs) provided. These arguments represent the fields you want to filter by.
- Creating: If no object is found with the given parameters, get_or_create will create a new object using the provided keyword arguments (**kwargs) and the additional optional keyword arguments (defaults) which are used to set field values for the new object.

The method returns a tuple with two elements:
- The object that was either retrieved from the database or created.
- A boolean indicating whether the object was created (True) or not (False).

Here's an example of how to use get_or_create:
```python
team, created = Team.objects.get_or_create(name='My Team', defaults={'some_field': 'value'})
```

In this example, get_or_create tries to find a Team object with the name 'My Team'. If it doesn't find one, it creates a new Team object with the provided name and sets some_field to 'value'. The team variable will hold the object, and created will be True if the object was created or False if it already existed and was just retrieved from the database.

**What Happens If defaults is Not Defined?**

If the object is not found based on the provided **kwargs, Django will attempt to create a new instance using only the values specified in **kwargs.

If defaults is omitted and the fields in **kwargs are sufficient to create a valid instance (i.e., they satisfy all required fields in the model), the instance will be created successfully.

If required fields are missing in **kwargs and you do not provide them via defaults, a __IntegrityError__ or __ValidationError__ might be raised during the creation process because the database will complain about missing mandatory fields.
