from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=100, null=True)
    email=models.EmailField(unique=True, null=True)
    age=models.PositiveIntegerField(null=True,blank=True)
    city=models.CharField(max_length=100, null=True)
    csv=models.TextField(null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class Application(models.Model):
    applicant=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    profession=models.CharField(max_length=100)
    education=models.TextField()
    work_experience=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    file=models.FileField(upload_to='application_files/', null=True, blank=True)


    def __str__(self):
        return self.profession
    
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    application=models.ForeignKey(Application,on_delete=models.CASCADE)
    body=models.TextField()
    file=models.FileField(upload_to='application_files/', null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']
    
    def __str__(self):
        return self.body[0:50]
    

# Create your models here.
