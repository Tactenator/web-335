/**
	Title: McLaurine-mongodbShell.js
    Author: Trevor McLaurine
    Date: 6/17/2023
    Description: Javascript file listing the required functions for assignment 4.3
 */


    // Loads the required Javascript file
    load("users.js")

    // Displays the full list of users in the document
    db.users.find()

    //Finds and displays the user with the specified email
    db.users.find({email: "jbach@me.com"})

    //Finds and displays the user with the specified last name
    db.users.find({lastName: "Mozart"})

    //Finds and displays the user with the specified first name
    db.users.find({firstName: "Richard"})

    //Finds and displays the specified employee ID
    db.users.find({employeeId: "1010"})

