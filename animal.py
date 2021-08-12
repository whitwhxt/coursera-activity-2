#chickens = 2 legs
#cows = 4 legs
#dogs = 4 legs

print ("How may Chickens?")
chicken = input()
print ("How many Cows?")
cow = input()
print ("How many Dogs?")
dog = input()

def animals(in1,in2, in3):
	chkleg = int(in1) * 2
	cowleg = int(in2) * 4
	dogleg = int(in3) * 4
	leoutput = chkleg + cowleg + dogleg
	return leoutput

print( animals(chicken, cow, dog), " legs")
