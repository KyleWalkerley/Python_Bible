#Ask user for name
name = input("What is your name?:")

#Ask user for age 
age = input("How old are you?:")

#Ask user for City
city = input("What city are you from?:")

#Ask user their favourate meal
meal = input("What is your favourate meal that you enjoy?:")
print(name)
print(age)
print(city)
print(meal)

#Create output text
string = "Your name is {} and you are {}.You come from {} and love's {}"
output = string.format(name, age, city, meal)
#Print output to screen
print(output)