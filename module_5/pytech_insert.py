from multiprocessing import connection
from pymongo import MongoClient

#https://github.com/Hadinski/csd-310

def insert_one():
    connection = MongoClient('mongodb+srv://admin:admin@cluster0.hkyt78c.mongodb.net/?retryWrites=true&w=majority')

    pytechdatabase = connection['pytech']

    studentCollection = pytechdatabase['students']

    student1 = {'first_name': 'Haydn', 'last_name': 'Hurst', 'student_ID': '1007' }
    student2 = {'first_name': 'John', 'last_name': 'Smith', 'student_ID': '1008' }
    student3 = {'first_name': 'Joe', 'last_name': 'Mama', 'student_ID': '1009' }

    student1_student_id = studentCollection.insert_one(student1).inserted_id
    student2_student_id = studentCollection.insert_one(student2).inserted_id
    student3_student_id = studentCollection.insert_one(student3).inserted_id

    print("Student 1 has been added to the students collection with document_id " + str(student1_student_id))
    print("Student 2 has been added to the students collection with document_id " + str(student2_student_id))
    print("Student 3 has been added to the students collection with document_id " + str(student3_student_id))

insert_one()



'''
MongoDB: insert_one() Example 
fred = {
 “first_name”: “Fred”
}
 
fred_student_id = students.insert_one(fred).inserted_id
 
print(fred_student_id)
 
MongoDB: find() Example 
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() Example 
doc = db.collection_name.find_one({“student_id”: “1007”})
 
print(doc[“student_id”])
'''