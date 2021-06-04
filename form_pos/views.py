from django.shortcuts import render
import psycopg2
from .forms import MyForm
from .models import Myform,Multi_File,Team_Lead
# Create your views here.
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
team_lead_list = [l[1] for l in team_record] 
print(team_lead_list)

def form_reg(request):
     if request.method == "POST":
        name = request.POST["name"]
        date = request.POST["date"]
        type = request.POST["reports"]
        lead = request.POST["team_lead"]
        hours = request.POST["no_of_hours"]
        progress = request.POST["today_progress"]
        todays_docs = request.FILES.getlist("todays_file")
        concerns = request.POST["concern"]
        next_plan = request.POST["next_plan"]
        next_docs = request.FILES.getlist("next-docs")

        report = Report(name=name, date=date, reports=type, team_lead=lead, no_of_hours=hours, todays_progress=progress, concerns=concerns, next_plan=next_plan)
        report.save()
        for f in todays_docs:
            print(f)
            document = Document(report=report, docs=f, type="T")
            document.save()

        for f in next_docs:
            document = Document(report=report, docs=f, type="N")
            document.save()







    if request.method == "POST" or None:
        print("one")    
        form = MyForm(request.POST or None,request.FILES or None)
        files=request.FILES.getlist('today_file')
        print("kk")
        if  form.is_valid():
            print("2")
            post= form.save(commit=False)
            form.save()
            for f in files:
                mul_file=Multi_File(f=post,images=f)
                mul_file.save()
            for f in todays_docs:
                print(f)
                document = Document(report=report, docs=f, type="T")
                document.save()       
            return render(request, 'form_pos/list.html', {'form':form})
        else:
            print("3")
            return render(request, 'form_pos/add.html',{'form':form})
    else:
        print("4")
        form = MyForm(request.POST or None,request.FILES or None)
        return render(request, 'form_pos/add.html',{'team_lead_list':team_lead_list,'form':form})                    