from django import forms
from form_pos.models import Myform
from form import settings
#Myform=Posts

REPORTS= [
    ('DAILY', 'DAILY'),
    ('WEEKLY', 'WEEKLY'),
    ('MONTHLY', 'MONTHLY'),
    ]

class DateInput(forms.DateInput):
    input_type='date'

class MyForm(forms.ModelForm,forms.DateInput):
    name = forms.CharField(error_messages={'required':'Please enter your 1'})
    date=forms.DateField(widget=DateInput)
    reports = forms.Select()
    team_lead = forms.Select()
    no_of_hours = forms.CharField(error_messages={'required':'Please enter your 5'})
    today_progress = forms.CharField(error_messages={'required':'Please enter your 6'})
    today_file = forms.FileField(error_messages={'required':'Please enter your 7'})
    concern = forms.CharField(error_messages={'required':'Please enter your 8'})
    next_plan = forms.CharField(error_messages={'required':'Please enter your 9'})
    next_file = forms.FileField(error_messages={'required':'Please enter your 10'},)
    
    class Meta:
        model = Myform
        fields = ('name','date','reports','team_lead','no_of_hours','today_progress','today_file','concern','next_plan','next_file')
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'}),
        }       


