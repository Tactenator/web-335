#Trevor McLaurine
#7/3/2023
#McLaurine_usersp2.py
#Web 335 - Assignment 7.3

#Importing MongoClient from pymongo
import pymongo
import datetime
import certifi

#Connection string to connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://web335_user:s3cret@web340db.93lxfky.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

#connect to web335DB
db = client['web335DB']

#initiates the collection to use
col = db['users']

# Creates a new user
newUser = {
    "firstName": "Bif",
    "lastName": "Jerky",
    "employeeId": "1013",
    "email": "Iambif@jerky.com",
    "dateCreated": datetime.datetime.now()
}

#inserts new user into the database
col.insert_one(newUser)

# Prints new user into the console.
print(col.find_one({ "employeeId": "1013" }))

# Updates users email
col.update_one(
    {"employeeId": "1013"},
    {
        "$set": {
            "email": "mynamebif@superbifboy.com"
        }
    }
)

# Prints new user information to the console.
print(col.find_one({ "email": "mynamebif@superbifboy.com" }))

# Deletes the user  
col.delete_one({ "employeeId": "1013"})

# Shows the user deleted
print(col.find_one({ "employeeId": "1013" }))