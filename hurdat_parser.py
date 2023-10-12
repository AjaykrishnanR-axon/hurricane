'''
	A python script written for parsing monthly cyclone hits from a cyclone tracking database called HURDAT2 
	which contains atmospheric and temporal parameters of cyclones from the year 1851. For our particular use
	case we had to find the number of cyclones on a monthly basis and the script below does exactly that. The 
	function below returns a dictionary containing the frequency of cyclones per month from the year 1851 to 
	2022.

'''

def parser(filePath):
	
	FILE = open(filePath, "r")
	lines = FILE.readlines()

	hurricaneName = ""

	monthlyCount = {}
	yearlyCount = {}

	yearCounter = ""
	monthCounter = ""

	months = {
		"01":"Jan",
		"02":"Feb",
		"03":"Mar",
		"04":"Apr",
		"05":"May",
		"06":"Jun",
		"07":"Jul",
		"08":"Aug",
		"09":"Sep",
		"10":"Oct",
		"11":"Nov",
		"12":"Dec"
	}


	for i in range(len(lines)):

		if lines[i].startswith("AL") or i == (len(lines) - 1):

			# hit a hurricane

			hurricaneName = lines[i].split(",")[0]
			hurricaneYear = hurricaneName[4:]

			if i != (len(lines) - 1):
				hurricaneMonth = lines[i+1].split(",")[0][4:6]

			if yearCounter == hurricaneYear:

				if monthCounter != hurricaneMonth:

					monthCounter = hurricaneMonth
					monthlyCount[months[hurricaneMonth]] = 1
				else:

					monthlyCount[months[hurricaneMonth]]+=1

			elif yearCounter == "":

				yearCounter = hurricaneYear
				monthlyCount[months[hurricaneMonth]] = 1

			elif i == (len(lines) - 1):
				yearlyCount[yearCounter] = monthlyCount

			else:

				yearlyCount[yearCounter] = monthlyCount
				yearCounter = hurricaneYear
				monthCounter = ""
				monthlyCount = {}
				monthlyCount[months[hurricaneMonth]] = 1

			i+=2 # skip 1 because all hurricanes have atleast 1 track record (stupid and useless but computers are human too !)

		else:

			i+=1

	return yearlyCount

if __name__ == "__main__":

	print(parser("./hurdat2-1851-2022-050423.txt"))
