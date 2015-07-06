import random

num = random.randint(1,10)

print "The computer Picked: %d" % (num)

userinput = input("Guess a Number: ")

print "You chose %d" % (userinput)

if (num == abs(userinput)):
	print "Yeah"
else:
	print "no"