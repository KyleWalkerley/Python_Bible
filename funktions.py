#functions

#Incorrect way
def add(x,y):
	x + y


#correct way
def add(x,y):
	return x + y

print(add(8,14))

#Storing variables as function answers
answer = add(95,20)
print(answer)

#print not the same as return
#print does not process return, only displays the answer

# Reverse
def rev(text):
	return text[::-1]

print(rev("spoon"))