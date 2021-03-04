# Unpacking arguments "*"
print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

# Unpack list before printing
# 5 mini arguments
print(*numbers)

# Unpack string
print("abc")
print(*"abc")
# print(*"abc") is the same as print("a","b","c")

# Packing arguments 
# Limited way
def add(x,y):
	return x + y

add(10,10)

# Better way
def add(*numbers):
	total = 0
	for number in numbers:
		total = total + number
	return(total)

print(add(1,2,3,4,5,6,7))

# Unpacking keyword arguments "**"

def about(name,age,likes):
	sentence = "Meet {}! They are {} years old and they enjoy {}".format(name, age, likes)
	return sentence

dictionary = {"name": "Kyle", "age": 19, "likes": "Python"}

print(about(**dictionary))


# packing keyword arguments
def foo(**kwargs):
	for key, value in kwargs.items():
		print("{}:{}".format(key, value))

foo(manna="Female", kyle = "Male", piet="Male")