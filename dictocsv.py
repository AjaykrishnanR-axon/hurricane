import ast

print("|YEAR|	|MONTH|	|NUMBER OF HURRICANES|")

FILE = open("./monthlyCountsHuOnly.txt", "r")

dict = ast.literal_eval(FILE.read())

FILE.close()

months = [
	"Jan",
	"Feb",
	"Mar",
	"Apr",
	"May",
	"Jun",
	"Jul",
	"Aug",
	"Sep",
	"Oct",
	"Nov",
	"Dec"
]

newDict = {}

for year in dict:
	yearlyCount = dict[f"{year}"]
	for month in months:
		if month not in yearlyCount:
			yearlyCount[month] = 0
	newDict[f"{year}"] = yearlyCount

for year in dict:
	for month in months:
		count = newDict[f"{year}"][month]
		print(f"{year},     {month},     {count}")


