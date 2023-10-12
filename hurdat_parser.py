import os

FILE = open("./hurdat2-1851-2022-050423.txt", "r")
lines = FILE.readlines()

totalHurricanes = 0

for i in range(len(lines)):
	if lines[i].startswith("AL"):
		# hit a hurricane
		totalHurricanes +=1
		i+=2
	else:
		i+=1
# print(len(lines))
print(totalHurricanes)
