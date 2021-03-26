from django.db import models

# Create your models here.
class employeeDetails(models.Model):
    employeeId=models.IntegerField(max_length=10,primary_key=True)
    firstName=models.CharField(max_length=50,allow_null=False)
    lastName=models.CharField(max_length=50, allow_null=False)
    addressLine1=models.CharField(max_length=100,allow_null=False)
    addressLine2=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    phoneNumber=models.IntegerField(max_length=12)
    startDate=models.DateTimeField()
    
