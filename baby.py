from random import choice

questions = ["Why do we need to brush our theeth:","Where does our poop go:", "Why is running faster than walking:"]


question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
	answer = input("why?: ").strip().lower()

print("Oh...Okay")