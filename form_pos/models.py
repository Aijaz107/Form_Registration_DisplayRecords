
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django import forms    
import psycopg2


connection = psycopg2.connect(user="postgres",
                            password="98499849",
                            host="127.0.0.1",
                            port="5432",
                            database="final_5")
cursor = connection.cursor()
postgreSQL_select_Query = "select * from form_pos_team_lead"

cursor.execute(postgreSQL_select_Query)
print("Selecting rows from Employeetable using cursor.fetchall")
team_record = cursor.fetchall() 
l=team_record
nl=[]
for i in range(len(l)):
    tl=[]
    for j in l[i]:
        if j==l[i][0]:
            pass
        else:
            tl.append(j)
    tl=tuple(tl)
    nl.append(tl)
print(nl)
# Create your models here.
REPORTS= [
    ('DAILY', 'DAILY'),
    ('WEEKLY', 'WEEKLY'),
    ('MONTHLY', 'MONTHLY'),
    ]
class Team_Lead(models.Model):
    title = models.CharField(max_length=50,blank=True)
    name = models.CharField(max_length=50,blank=True)
    

class Myform(models.Model):
    name = models.CharField(max_length=100)
    date=models.DateField(blank=True, null=True,default='')
    reports = models.CharField(max_length=50,choices=REPORTS, default='')
    team_lead= models.CharField(max_length=20,choices=nl, default='')
    no_of_hours = models.CharField(max_length=100)
    today_progress = models.CharField(max_length=100)
    today_file = models.FileField(max_length=100,default='')
    concern = models.CharField(max_length=500)
    next_plan = models.CharField(max_length=500)
    next_file = models.FileField(max_length=100,default='')

class Multi_File(models.Model):
    f=models.ForeignKey(Myform, on_delete=models.CASCADE)
    images=models.FileField(upload_to="form_pos/",blank=True,null=True)
                            

