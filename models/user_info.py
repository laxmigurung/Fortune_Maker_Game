import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Iamhappy0610#",
  database="UserInformation"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (firstName VARCHAR(255), lastName VARCHAR(255),Email VARCHAR(255),"
                 "DateOfBirth VARCHAR(255))")
