from pymongo import MongoClient

#https://github.com/Hadinski/csd-310

url = "mongodb+srv://admin:admin@cluster0.hkyt78c.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

mydb = client.pytech

pytech = mydb['pytech']

mycollection = mydb.students

for document in mycollection.find():
    print(document)

filter = {'student_ID': '1007'}
newValues = {"$set": {'last_name': 'not_Hurst'}}
mycollection.update_one(filter, newValues)

result = mycollection.find_one({'student_ID': '1007'})
print(result)
