movies = {
	"Fourius 9":[18,8],
	"Spiderman":[13,12],
	"Borat":[16,4],
	"Ben 10":[3,24]	
}

while True:
	choice = input("What movie do you want to watch today?: ").strip()

	if choice in movies:

		age = int(input("Please enter your age here.").strip())
		#Check user age
		if age >= movies[choice][0]:
			#check seats available
			if movies[choice][1]>0:
				print("Welcome and enjoy!")
				movies[choice][1] = movies[choice][1] -1
			else:
				print("Sorry we are sold out.")
		else:
			print("You are too young for the film.")

	else:
		print("We are not showing that movie currently.")