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
					# Check each value in a row and add it if it can be a float

			dict_names.update({row[0]:rowsSum})

	return dict_names
	
def sumColumns(filename):
	dict_names = {}
	numList = []
	name0 = 0
	name1 = 0
	name2 = 0
	name3 = 0

	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)
		row1 = next(rdr)
		columnsNum = len(row1)

		# Need to get it to work dynamically but for loop in while doesn't work  
		for row in rdr:
			name0 += float(row[0])
			name1 += float(row[1])
			name2 += float(row[2])

		dict_names.update({row1[0]:name0})
		dict_names.update({row1[1]:name1})
		dict_names.update({row1[2]:name2})
		dict_names.update({row1[3]:name3})

	return dict_names



def isfloat(value):

	# Check if list item can be a float
	try:
		float(value)
		return True
	except ValueError:
		return False

import csv

import doctest
doctest.testmod()