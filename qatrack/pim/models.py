import os
import datetime
from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


def content_file_name(instance, filename):
    return '/'.join(['user_upload', str(instance.submitter.username), str(instance.incident_date), filename])

class practice_improvement(models.Model):
    THERAPIST = 'Therapist'
    DOSIMETERIST = 'Dosimeterist'
    PHYSICIST = 'Physicist'
    PHYSICIAN = 'Physician'
    NURSE = 'Nurse'
    STAFF = 'Staff'
    RAD_ONC_CHOICES = (
        
        (THERAPIST, 'Therapist'),
        (DOSIMETERIST, 'Dosimeterist'),
        (PHYSICIST, 'Physicist'),
        (PHYSICIAN, 'Physician'),
        (NURSE, 'Nurse'),
        (STAFF, 'Staff'),
        
     )
    
    patient_ID = models.IntegerField()
    incident_date = models.DateField('Date of Event',default=datetime.date.today)
    report_date = models.DateTimeField(auto_now=True)
    submitter = models.ForeignKey(User)
    department = models.CharField(max_length=13,
                                  choices=RAD_ONC_CHOICES,
                                  default=PHYSICIST)
    comment = models.TextField(max_length=1000)
    pim_image = models.FileField(upload_to=content_file_name, blank=True, null=True)
    
class DateInput(forms.DateInput):
    input_type = 'date'
    
class practice_improvementForm(ModelForm):
    
    pim_image = forms.FileField(label='Select a file',required=False)
   
    class Meta:
        model = practice_improvement
        exclude = ['submitter']
        widgets = {
            'incident_date': DateInput()
        }
