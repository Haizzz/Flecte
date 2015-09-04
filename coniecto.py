# analysis and prediction
# read data.json
import json
import statistics
meanPrice = []
trend = []
nameList = ["cba", "nab", "anz", "wbc", "wow", "jbh", "wes", "asx", "bhp", "ccl", "dmp"]
# number crunching
def priceMean(name):
	with open('data.json', 'r+') as f:
		jsonData = json.load(f)
		meanPrice.append(statistics.mean(jsonData["price"][name]))
# trend finding | last 2 days
def trend2d(name):
	with open('data.json', 'r+') as f:
		jsonData = json.load(f)
		if jsonData["change"][name][-1] > jsonData["change"][name][-2]:
			if jsonData["change"][name][-1] > 0 and jsonData["change"][name][-2] > 0:
				trend.append(["increase", "continuing",jsonData["change"][name][-1] - jsonData["change"][name][-2]])
			elif jsonData["change"][name][-1] > 0 and jsonData["change"][name][-2] < 0:
				trend.append(["increase", "continuing", jsonData["change"][name][-1] - jsonData["change"][name][-2]])
			elif jsonData["change"][name][-1] < 0 and jsonData["change"][name][-2] < 0:
				trend.append(["decrease", "continuing", jsonData["change"][name][-1] - jsonData["change"][name][-2]])
		elif jsonData["change"][name][-1] < jsonData["change"][name][-2]:
			if jsonData["change"][name][-1] > 0 and jsonData["change"][name][-2] > 0:
				trend.append(["increase", "slowing", jsonData["change"][name][-2] - jsonData["change"][name][-1]])
			elif jsonData["change"][name][-1] < 0 and jsonData["change"][name][-2] > 0:
				trend.append(["decrease", "continuing", jsonData["change"][name][-2] - jsonData["change"][name][-1]])
			elif jsonData["change"][name][-1] < 0 and jsonData["change"][name][-2] < 0:
				trend.append(["decrease", "slowing", jsonData["change"][name][-2] - jsonData["change"][name][-1]])
		print(name, jsonData["change"][name][-2], jsonData["change"][name][-1])
# calling functions
for i in nameList:
	priceMean(i)
for i in nameList:
	trend2d(i)
# debug prints
trend2d("wes")
print("""

-------------------------number crunching-------------------------

""")
print(meanPrice)
print(trend)
print("""

-------------------------current state-------------------------

""")
print("name", end='')
print("    {:^5}".format("price"), end='')
print("    {:^15}".format("rise/fall"), end='')
print("{:^20}".format("++/--"), end='')
print("{:^15}".format("degree"))
print("")
for i in range(len(nameList)):
	print(nameList[i], end='')
	print("  |  ${:^5.2f}".format(meanPrice[i]), end='')
	print("  |  {:^10}".format(trend[i][0], " | "), end='')
	print("  |  {:^15}".format(trend[i][1]), end='')
	print("  |  {:^20.2f}".format(trend[i][2]))









