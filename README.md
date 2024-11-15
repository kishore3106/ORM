# Ex02 Django ORM Web Application
## Date: 25-10-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-10-26 144424.png>)



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

```
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


```


## OUTPUT
![alt text](<Screenshot (1).png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
