# Ex02 Django ORM Web Application
## Date: 26-10-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![Screenshot 2024-10-26 144424](https://github.com/user-attachments/assets/54294fe7-b6bb-48df-bac6-7f1029a57a8e)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

'''
admin.py 

from django.contrib import admin
from .models import Loan, LoanAdmin
admin.site.register(Loan, LoanAdmin)

models.py

from django.db import models
from django.contrib import admin
class Loan(models.Model):
	Name=models.CharField(max_length=20)
	Acc_No=models.IntegerField(primary_key=True)
	Dob=models.DateField()
	Email=models.EmailField()
	Balance=models.FloatField(default=0)
class LoanAdmin(admin.ModelAdmin):
	list_display=('Name','Acc_No','Dob','Email','Balance')


'''


## OUTPUT

![Screenshot (1)](https://github.com/user-attachments/assets/12605353-03de-45da-8a3a-59a148d80362)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
