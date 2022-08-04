import mysql.connector
user="root"
password="@Eastlands9!"
host="127.0.0.1"

cnx = mysql.connector.connect(user="root", password="@Eastlands9!", host="127.0.0.1", database="Project_1")
cursor = cnx.cursor()

query_customers= "SELECT * FROM customers"
cursor.execute(query_customers)

for record in cursor:
    print("The Records in the file are :")
    print(record)
    print(record[3])
    age = int(input("enter age"))
    if record[3]== age:
        print("\nWelcome to the store :")
        print("\t1) Add Customer ")
        print("\t2) View Customer Records ")
        print("\t3) View Order Records  ")
        print("\t4) Add new Admin")
        print("\t5) Add new Computer to system ")
        print("\t6) View Order Records ")
        selection = input("select option Admin ")
    else:
        print("No its not")

cursor.close()

