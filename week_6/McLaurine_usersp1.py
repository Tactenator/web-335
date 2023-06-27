#Trevor McLaurine
#6/26/2023
#McLaurine_usersp1.py
#Web 335 - Assignment 6.3

#Importing MongoClient from pymongo
from pymongo import MongoClient

#Connection string to connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@web340db.93lxfky.mongodb.net/?retryWrites=true&w=majority")

#connect to web335DB
db = client['web335DB']

#initiates the collection to use
col = db['users']

#Finds all users in the collection and prints them to the console
for document in col.find({}):
    print(document)

#searches for and prints document with specified employeee id
print(col.find_one({ 'employeeId': '1011' }))

#searches for and prints document with specified last name
print(col.find_one({ 'lastName': 'Mozart'}))