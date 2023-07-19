#Trevor McLaurine
#7/19/2023
#McLaurine_console.py
#Web 335 - Assignment 9.2

#Importing MongoClient from pymongo
import pymongo

# Kept receiving error that stated certificate was invalid. Imported this to solve the problem. 
import certifi

print("*****************************************************")
print("************* Welcome to What-A-Book! ***************")
print("*****************************************************")

print("Connecting to MongoDB....\n")

#Connection string to connect to MongoDB. Certifi fixes certification issues
client = pymongo.MongoClient("mongodb+srv://web335_user:s3cret@web340db.93lxfky.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

if(client):
    print("Success!\n")

#connect to web335DB
db = client['web335DB']

print("Connecting to database...\n")

#initiates the collection to use
books = db['books']
customers = db['customers']

print("Database connected. Retrieving book list...\n")

bookList = db.books.find({ })

for document in bookList:
    print("BookID: " + str(document.get('bookId')))
    print("Title: " + str(document.get('title')))
    print("Genre: " + str(document.get('genre')))
    print("Author: " + str(document.get('author')))
    print("\n ******************************************************* \n")

run_app = True
print("How can we help you today?\n To search by genre, type 'genre'. To display a customer's wishlist, type 'wishlist' .")
print("If you wish to exit, type 'exit' ")

while(run_app):
    user_input = input("What would you like to do?: ")
    if(user_input == "genre"):
        print("Please choose from fantasy, fiction, science fiction, or historical fiction")
        input("What Genre would you like to search for?: ")
        if("fantasy"):
            print("You chose fantasy")
    elif(user_input == "wishlist"):
        input("Please input the customer ID of the wishlist you wish to see: ")
    elif(user_input == "exit"):
        print("Thank you for using the What-a-book app! Good-bye!")
        run_app = False
    else:
        print("Unknown input. Please try again.")
        continue

