import csv
import os
import pymysql

#1ST METHOD
#opens and reads csv file via iteration
with open(raw_input("Input a file path please: ")) as input_file:
		
	#tells you what directory your file is in
	print("You chose this directory that your file is in: " + os.path.realpath(raw_input()))
	#adds space for more readability
	print(" ")

	#using a reader, iterate through file 
	#will use thisReader variable to call on below with the sql connector method
	thisReader = csv.reader(input_file) #uses built in reader object
	for i in thisReader:
		print i
	print("\n" "END of file contents" "\n")

####################################################################################

#SECOND METHOD 
#connects to mySQL database
mydb = pymysql.connect(host="localhost",
    user="root",
    passwd="root",
    db="mydb")

#goes over database
cursor = mydb.cursor()

#reads over input file uses iteration
csv_data = csv.reader(file(input_file))
for j in csv_data:

    cursor.execute('INSERT INTO testcsv(first name, last name, location, job )' \
          'VALUES("%s", "%s", "%s", "%s")',j)
    
#close the connection to the database.
mydb.commit()
cursor.close()
print "Complete"

















