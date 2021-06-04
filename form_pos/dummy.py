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
print(employee_records[1][0]


if 1:
    print("ljdlbj")
if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")