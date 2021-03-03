known_users = ["Jan", "Freek", "Martin", "Jessica", "Makayla", "Divan", "Mariska", "Sonica"]

#print(len(known_users))

while True:
	print("Hi my name is Kyle")
	name = input("What is your name?: ").strip().capitalize()

	if name in known_users:
		print("Hello {}.".format(name))
		remove = input("Would you like to be removed from the system (y/n)?:").strip().lower()

		if remove == "y":
			known_users.remove(name)
		elif remove == "n":
			print("OK I didnt want you to GO anyway.")

	else:
		print("Unknown user recognised.Do you want me to register you {}".format(name))
		add_me = input("Are you ready to be registered to the system (y/n)?:").strip().lower()
		if add_me == "y"
			known_users.append(name)
		elif add_me == "n":
			print("Ok enjoy your day and see later.")