def createNW(coordinates):
	
	if coordinates[0] < 0:
		letterNS = "S"
	else:
		letterNS = "N"

	if coordinates[1] < 0:
		letterEW = "W"
	else:
		letterEW = "E"

	north1 = int(coordinates[0])
	north2 = (coordinates[0] - north1) * 60
	if north1 < 0 or north2 < 0:
		north1 *= -1
		north2 *= -1
	north = float(str(north1) + str(north2))

	west1 = int(coordinates[1])
	west2 = (coordinates[1] - west1) * 60
	if west1 < 0 or west2 < 0:
		west1 *= -1
		west2 *= -1
	west = float(str(west1) + str(west2))
	
	return (north, letterNS, west, letterEW)


def createDecimal(coordinates):

	northHours = coordinates[0] // 100
	northMinutes = coordinates[0] % 100
	if coordinates[1] == 'S':
		north = -(northHours + northMinutes / 60)
	else:
		north = northHours + northMinutes / 60
	
	southHours = coordinates[2] // 100
	southMinutes = coordinates[2] % 100
	if coordinates[3] == 'W':
		south = -(southHours + southMinutes / 60)
	else:
		south = southHours + southMinutes / 60

	return (round(north, 2), round(south, 2))

question = raw_input("""
Which coordinate to convert: 
(1) With NW to Decimal
(2) With Decimal to NW
>>> """)

if int(question) == 1:
	coordinates = raw_input("Enter Coordinates in format 1043.2 N 7532.4 W: ")
	coordinates = coordinates.split(" ")
	coorTuple = (float(coordinates[0]), coordinates[1], float(coordinates[2]), coordinates[3])
	answer = createDecimal(coorTuple)
	print "The coordinate is:", answer
elif int(question) == 2:
	coordinates = raw_input("Enter Coordinates in format 10.432,-75.32: ")
	coordinates = coordinates.split(",")
	coorTuple = (float(coordinates[0]), float(coordinates[1]))
	answer = createNW(coorTuple)
	print "The coordinate is:", answer	
else:
	print "Wrong choice"