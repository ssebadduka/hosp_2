from django.db import models

class Month(models.TextChoices):
        JAN = 'Male', "Male"
        FEB = 'Female', "Female"
        

class Patient(models.Model):
    patient_name = models.CharField(max_length=45)
    patient_code = models.CharField(max_length=45,unique=True)
    complain = models.CharField(max_length=45)
    gender = models.CharField(max_length=45,choices=Month.choices,default=Month.JAN)
    address = models.CharField(max_length=45)
   # country = models.CharField(max_length=45 ,default="Uganda")
   # year_of_birth = models.IntegerField()
    #is_in_patient = models.BooleanField(default=False)

    
class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE) 
    date_of_diagnosis = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=45 ,null=True)
    
# Create your models here.
