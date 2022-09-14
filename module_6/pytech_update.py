from pymongo import MongoClient
import pprint

#https://github.com/Hadinski/csd-310

url = "mongodb+srv://admin:admin@cluster0.hkyt78c.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

mydb = client.pytech

pytech = mydb['pytech']

mycollection = mydb.students

print('Student documents from find() query: \n')

for document in mycollection.find():
    pprint.pprint(document)

filter = {'student_ID': '1007'}
newValues = {"$set": {'last_name': 'not_Hurst'}}
mycollection.update_one(filter, newValues)

print('\nStudent document 1007: \n')
result = mycollection.find_one({'student_ID': '1007'})
pprint.pprint(result)
