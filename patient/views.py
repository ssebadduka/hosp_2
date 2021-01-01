from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import Register_patient
from .forms import Patient
from django.contrib import messages

# this function add patient in database
def add_show(request):
    if request.method == 'POST':
        fm = Register_patient(request.POST)
        if fm.is_valid():
          pn =  fm.cleaned_data['patient_name']
          pc =  fm.cleaned_data['patient_code']
          cp =  fm.cleaned_data['complain']
          gn =  fm.cleaned_data['gender']
          ad =  fm.cleaned_data['address']
          print(pn)
          preg = Patient(patient_name=pn, patient_code=pc, complain=cp, gender=gn, address=ad)
          preg.save()
          messages.success(request,'Patient Successfuly Registered')
        fm = Register_patient()
    else:
        fm = Register_patient()
    pat = Patient.objects.all()
    return render(request,'patient/addandshow.html', {'form':fm, 'pati':pat })

# # this function edit/update patient in database
def update_pat(request,id):
    if request.method == 'POST':
        pi = Patient.objects.get(pk=id)
        fm = Register_patient(request.POST,instance=pi)
        if fm.is_valid():
         fm.save()
         messages.success(request,'Patient Updted Successfuly ')
    else:
        pi = Patient.objects.get(pk=id)
    fm = Register_patient(instance=pi)
    return render (request,'patient/updatepatient.html', {'form':fm})

# # this function delete patient in database
def delete_pat(request,  id):
    if request.method=='POST':
        pi = Patient.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
