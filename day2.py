#!/usr/bin/python

def day2_partone(row):
	'''
	For each row, determine the difference between the largest 
	value and the smallest value; the checksum is the sum of 
	all of these differences.
	'''
	smallest = 0
	largest = 0
	for counter, item in enumerate(row):
		i = int(item)
		# print "item: %s" % (i)
		if counter == 0:
			smallest = i
			largest = i
		else:
			if i <= smallest:
				smallest = i
				# print "smallest: %s" % (smallest)
			if i >= largest:
				largest = i
				# print "largest: %s" % (largest)
		# print "largest: %s smallest: %s" % (largest, smallest)
	difference = largest - smallest

	return difference


def day2_parttwo(row):
	'''
	the goal is to find the only two numbers in each row where 
	one evenly divides the other - that is, where the result 
	of the division operation is a whole number. They would like
	 you to find those numbers on each line, divide them, and 
	 add up each line's result.
	'''
	for counter, item in enumerate(row):
		row_to_check = [x for i,x in enumerate(row) if i!=counter]
		for row_counter, row_item in enumerate(row_to_check):
			x = (row[counter] % row_item)
			print "counter: %s X: %s row[counter]: %s row_item: %s" % (counter, x, row[counter], row_item)
			if x is None:
				print "match"
				return row_item





myTestArray = [ [5, 1, 9, 5], [7,5,3], [2,4,6,8] ]
myRealArray = [
[1640,590,93,958,73,1263,1405,1363,737,712,1501,390,68,1554,959,79],
[4209,128,131,2379,2568,2784,2133,145,3618,1274,3875,158,1506,3455,1621,3799],
[206,1951,2502,2697,2997,74,76,78,1534,81,2775,2059,3026,77,2600,3067],
[373,1661,94,102,2219,1967,1856,417,1594,75,100,2251,2200,1825,1291,1021],
[57,72,51,1101,1303,60,1227,421,970,1058,138,333,1320,1302,402,1210],
[4833,5427,179,3934,4533,5124,4832,2088,94,200,199,1114,4151,1795,208,3036],
[759,876,110,79,1656,1691,185,544,616,312,757,1712,92,97,1513,1683],
[1250,1186,284,107,1190,1233,573,1181,1041,655,132,547,395,146,119,515],
[505,1726,79,180,86,1941,1597,1785,1608,1692,968,1177,94,184,91,31],
[1366,2053,1820,1570,70,506,53,415,717,1263,82,366,74,1255,2020,1985],
[2365,5585,2285,4424,5560,3188,3764,187,88,223,1544,5023,4013,5236,214,196],
[1487,1305,1359,1615,6579,2623,4591,150,5030,188,146,4458,5724,5828,1960,221],
[3114,688,3110,334,1921,153,4083,131,2234,3556,3573,3764,127,919,3293,104],
[1008,78,1196,607,135,1409,296,475,915,157,1419,1304,153,423,163,704],
[235,4935,4249,3316,1202,221,1835,380,249,1108,1922,5607,4255,238,211,3973],
[1738,207,179,137,226,907,1468,1341,1582,1430,851,213,393,1727,1389,632]
]
myTestArrayTwo = [ [5, 9, 2, 8], [9, 4, 7, 3,], [3, 8, 6, 5] ]

total = 0
print "Day two; part One"
for counter, row in enumerate(myTestArray):
	result_row = day2_partone(row)
	total = (total + result_row)
	print "TestArray counter: %s total: %s" % (counter, result_row)

print "total: %s" % (total)

total = 0
for counter, row in enumerate(myRealArray):
	result_row = day2_partone(row)
	total = (total + result_row)
	print "RealArray counter: %s total: %s" % (counter, result_row)

print "total: %s" % (total)

total = 0
print "Day two; part two"
for counter, row in enumerate(myTestArrayTwo):
	result_row = day2_parttwo(row)
	total = (total + result_row)
	print "TestArrayTwo counter: %s total: %s" % (counter, result_row)

print "total: %s" % (total)

