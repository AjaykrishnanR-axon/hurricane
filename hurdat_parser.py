import os

def parser(FILE):
	pass

FILE = open("./hurdat2-1851-2022-050423.txt", "r")
lines = FILE.readlines()

totalHurricanes = 0
# returnList = {"year": {"month":"count"}}
totalNames = []

for i in range(len(lines)):
	if lines[i].startswith("AL"):
		# hit a hurricane
		hurricaneName = lines[i].split(",")[0]
		totalHurricanes +=1
		totalNames.append(hurricaneName)
		i+=2 # skip 1 because all entries have atleast 1 track record
	else:
		i+=1
# print(len(lines))
print(totalHurricanes)
print(totalNames)
