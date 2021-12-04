from django.db import models
from django.db import models
from datetime import datetime, timedelta
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')
        if not  FIRST_NAME_REGEX.match(postData['first_name']):    # test whether a field matches the pattern            
            errors['first_name_format'] = ("Invalid name")
        
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'

        # Email validation
        # Pattern Validation
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Invalid email address"

        # Duplicate email
        email_check=User.objects.filter(email=postData['email'])
        if email_check:
            errors['duplicate']="Invalid email already taken"
            
        # Check for Password 
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match'
        
        return errors
    def register(self, postData):
        # Encrypt password
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        # 12345678
        return User.objects.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw,
        )
    def authenticate(self, email, password):
        # filter user based on given email
        users=User.objects.filter(email=email)
        if users:
            user=users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return True
            else:
                return False
        return False
        
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = UserManager()

class ClubManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Name must have at least 3 characters."        
        if len(postData['desc']) == 0:
            errors["desc"] = "Description is empty"
        return errors

class Club(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    owner = models.ForeignKey(User, related_name = "clubs",on_delete=models.CASCADE)
    joined = models.ManyToManyField(User, related_name = "joined_clubs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)            
    objects= ClubManager()