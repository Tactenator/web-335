/**
	Title: McLaurine-AggregateQueries.js
    Author: Trevor McLaurine
    Date: 6/28/2023
    Description: Javascript file listing the required functions for assignment 6.2
 */


    // Loads the required Javascript file
    load("houses.js")

    //Finds all documents in the houses collection
    db.houses.find({})

    //Finds all documents in the students collection
    db.students.find({})

    // Creates a new student document and adds it to the collection.
    db.students.insertOne({
        'firstName': "Draco",
        "lastName": "Malfoy",
        "studentId": "sl100",
        "houseId": "h1010"
    })

    //Deletes the previously created student document in the student collection
    db.students.deleteOne({ "_id": ObjectId("649b46bebe1e514f317997d3")})

    //Shows students by their house
    db.houses.aggregate([
        { $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "house"
        }}
    ])

    //Shows students that belong in the houseId of Gryffindor
    db.houses.aggregate([
        { $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "house"
        }},
        { $match: {
            "house.houseId": "h1007"
        }}
    ])

    //Shows students whose house mascot is the Eagle
    db.houses.aggregate([
        { $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "house"
        }},
        { $match: {
            "mascot": "Eagle"
        }}
    ])
