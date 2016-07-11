
from random import randint

def generate(v):
	input = [[randint(1,100) for i in range(v)] for i in range(2)]
	sum = [x + y for x, y in zip(input[0], input[1])]
	f = open("test_"+str(v)+".txt","a")

	for output in input[0]:
		f.write("%s,"%output)
	f.write("\n")

	for output in input[1]:
		f.write("%s,"%output)
	f.write("\n")
	
	for output in sum:
		f.write("%s,"%output)
	f.write("\n")

	f.close()

	


generate(10)
generate(20)
generate(50)
generate(100)
