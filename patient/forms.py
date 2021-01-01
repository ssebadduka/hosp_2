from django.core import validators
from django import forms
from .models import Patient

class Register_patient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name','patient_code','complain','gender','address']

        widgets= {
            'patient_name'  : forms.TextInput(attrs={'class':'form-control'}),
            'patient_code' : forms.TextInput(attrs={'class':'form-control'}),
            'complain'  : forms.TextInput(attrs={'class':'form-control'}),
            'gender'  : forms.TextInput(attrs={'class':'form-control'}),
            'address'  : forms.TextInput(attrs={'class':'form-control'}),
        }