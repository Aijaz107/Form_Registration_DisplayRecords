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
employee_records = cursor.fetchall() 

print("Print each row and it's columns values")
print(employee_records)
print(employee_records[0][0])
print(employee_records[0][1])
print(employee_records[1][0])

#for row in mobile_records:
#   print(row)

#except (Exception, psycopg2.Error) as error :
 #   print ("Error while fetching data from PostgreSQL", error)

#finally:
    #closing database connection. 
pswd_list = [l[1] for l in employee_records] 
#print(pswd_list)
l=employee_records
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
if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")