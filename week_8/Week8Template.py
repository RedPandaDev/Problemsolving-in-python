"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***

def sumRows(filename, header=False):
    # Add code here
	dict_names = {}
	numList = []

	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)

		if header == True:
			next(rdr)  # skip header row

		for row in rdr:
			numList = row[1::]
			rowsSum = 0

			for i in numList:
				if isfloat(i) == True:
					rowsSum += float(i)

			dict_names.update({row[0]:rowsSum})

	return dict_names
	
def sumColumns(filename):
	# dict_names = {}
	# numList = []

	# with open(filename) as csvfile:
	# 	rdr = csv.reader(csvfile)

	# 	for row in rdr:
	# 		numList = row[1::]
	# 		rowsSum = 0

	# 		for i in numList:
	# 			if isfloat(i) == True:
	# 				rowsSum += float(i)

	# 		dict_names.update({row[0]:rowsSum})

	# return dict_names



def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

import csv

import doctest
doctest.testmod()