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


