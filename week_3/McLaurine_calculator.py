#initializing functions for add, subtract, divide, and multiply
def add(x, y): 
    return (x + y);

def subtract(x, y):
    return (x - y);

def divide(x, y):
    return (x / y)

def multiply(x, y):
    return (x * y); 

#initializes variables by calling functions.
newSum = add(8, 1); 
product = multiply(3, 2);
difference = subtract(7, 4); 
quotient = divide(9, 3); 

#Variable used for concatenating a string to display the results of each function.
output = 'Addition: ' + str(newSum) + '\nSubtraction: ' + str(difference) + '\nMultiplication: ' + str(product) + '\nDivision: ' + str(quotient);

#prints the output variable
print(output)

#prevents the app from closing. 
input(" ")