def add(x, y): 
    return (x + y);

def subtract(x, y):
    return (x - y);

def divide(x, y):
    return (x / y)

def multiply(x, y):
    return (x * y); 

newSum = add(8, 1); 
product = multiply(3, 2);
difference = subtract(7, 4); 
quotient = divide(9, 3); 

output = 'Addition: ' + str(newSum) + '\nSubtraction: ' + str(difference) + '\nMultiplication: ' + str(product) + '\nDivision: ' + str(quotient);

print(output)

input(" ")