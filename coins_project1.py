# Class is a base template for object
# Objects act independently from each other

#class Pound:

	#States
	#value = 1.00
	#colour = "gold"
	#num_edges = 1
	#diameter = 22.5 #mm
	#thickness = 3.15 #mm
	#heads = True



#coin1 = Pound()
#print(coin1.colour)
#coin1.colour = "blue"
#print(coin1.colour)

#coin2 = Pound()
#print(coin2.colour)

import random

class Pound:

	# Methods
	# Constructuring states
	def __init__(self, rare=False):

		self.rare = rare

		if self.rare:
			self.value = 1.25
		else:
			self.value = 1.00

		self.colour = "gold"
		self.num_edges = 1
		self.diameter = 22.5 #mm
		self.thickness = 3.15 #mm
		self.heads = True


	def __del__(self):
		print("Coin Spent!")

	def rust(self):
		self.colour = "greenish"

	def clean(self):
		self.colour = "gold"

	def flip(self):
		heads_options = [True, False]
		choice = random.choice(heads_options)
		self.heads = choice