#Global variable scope
a = 95

def f1():
	print(a)

def f2():
	print(a)

f1()
f2()

#Local variable scope
def f1():
	a = 95
	print(a)

def f2():
	a = 50
	print(a)

f1()
f2()

# Global and local combined
# created local variable called a
# Stops global variable being overridden

# Global variables can't be changed from within local scopes 
a = 289

def f1():
	a = 78
	print(a)

def f2():
	a = 50
	print(a)

f1()
f2()
print(a)

# Another example
a = 250

def f1():
	b =  a + 50
	print(b)

def f2():
	a = 50
	print(a)

f1()
f2()
print(a)

# Overriding global from within local
a = 250

def f1():
	global a
	a =  100 # Global (new)
	print(a)

def f2():
	a = 50 # Local
	print(a)

f1()
f2()
print(a)


# overriding within a list
a = [1,2,3]

def f1():
	a[0] = 5
	print(a)

def f2():
	a = 50 # Local
	print(a)

f1()
f2()
print(a)