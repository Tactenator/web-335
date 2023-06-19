#Trevor McLaurine
#6/19/2023
#McLaurine - hobbies.py
#Web 335 - Assignment 4.3

#Initializing an list of hobbies in an array
hobbies = ['Biking', 'Cooking', 'Music', 'Gaming', 'Sewing']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#Begins the for loop to iterate over the array and print the value to the console
for x in hobbies:
    print(x)

# Begins the for loop to iterate over the days of the week in the days array
for day in days: 
    # Checks to see if the day is equal to Sunday or Saturday
    if day == 'Sunday' or day == 'Saturday':
        #if true, prints a message to go enjoy hobbies
        print('No work today! Go enjoy your hobbies!')
    else:
        #if false, prints a message to say it is a work day.
        print('No hobbies today. Today is a work day...')