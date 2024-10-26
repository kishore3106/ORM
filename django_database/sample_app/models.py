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
