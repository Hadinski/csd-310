from pymongo import MongoClient
import pprint

#https://github.com/Hadinski/csd-310

url = "mongodb+srv://admin:admin@cluster0.hkyt78c.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

mydb = client.pytech

pytech = mydb['pytech']

mycollection = mydb.students

#Print all documents
print('\nStudent documents from find() query: \n')
for document in mycollection.find():
    pprint.pprint(document)

#Insert new student
connection = MongoClient('mongodb+srv://admin:admin@cluster0.hkyt78c.mongodb.net/?retryWrites=true&w=majority')
pytechdatabase = connection['pytech']
studentCollection = pytechdatabase['students']

studentX = {'first_name': 'Jesse', 'last_name': 'McCree', 'student_ID': '1010' }
studentX_student_ID = studentCollection.insert_one(studentX).inserted_id

print("\nThe new student has been added to the students collection with document_id " + str(studentX_student_ID), '\n')

#find.one() for new student
print('\nNew student document: \n')
result = mycollection.find_one({'student_ID': '1010'})
pprint.pprint(result)

#deleting new student
deletedStudent = {'student_ID': '1010'}
mycollection.delete_one(deletedStudent)

#Printing all documents again
print('\nStudent documents from find() query: \n')
for document in mycollection.find():
    pprint.pprint(document)
