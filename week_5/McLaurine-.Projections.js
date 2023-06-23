/**
	Title: McLaurine-Projections.js
    Author: Trevor McLaurine
    Date: 6/21/2023
    Description: Javascript file listing the required functions for assignment 5.2
 */

    //Inserts a new user into the user database.
    db.users.insertOne({
        firstName: 'Yarg',
        lastName: 'Blargensen',
        employeeId: '12345',
        email: 'yarg@blarg.com',
        dateCreated: new Date()
    })

    // Updates the email of the person with the object ID specified.
    db.users.updateOne(
        { _id: ObjectID('') },
        { $set: { email: 'mozart@me.com' }}
        )

    //finds users with the specified $project fields.
    db.users.aggregate(
        {
            $project: {
                "firstName": 1,
                "lastName": 1,
                "email": 1
            }
        }
    )
