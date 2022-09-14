from unittest import result
from pymongo import MongoClient

#https://github.com/Hadinski/csd-310

url = "mongodb+srv://admin:admin@cluster0.hkyt78c.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

mydatabase = client.pytech

pytech = mydatabase['pytech']

mycollection = mydatabase.students

result1 = mycollection.find_one({'student_ID': '1007'})
result2 = mycollection.find_one({'student_ID': '1008'})
result3 = mycollection.find_one({'student_ID': '1009'})

print(result1, '\n', result2, '\n', result3)