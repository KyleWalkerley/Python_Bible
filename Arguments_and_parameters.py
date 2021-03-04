# Parameters represented by name, age, likes

def about(name, age, likes):
	sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
	return sentence

print(about("Morne", 17, "Python"))

# Keyword argument
print(about(name = "Morne", age = 17, likes = "Python"))

# Setting a default value
# default values must go last
def about(name, age, likes = "Python"):
	sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
	return sentence

print(about("Morne", 17))

# Can be overridden
print(about("Calvin", 19, "Rugby"))