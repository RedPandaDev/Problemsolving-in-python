
def hms(totalSeconds):
	seconds = totalSeconds % 60
	totalMinutes = totalSeconds // 60
	minutes = totalMinutes
	hours = totalMinutes // 60
	minutes = totalMinutes % 60
	delimiter = ':'
	print(hours,delimiter, minutes,delimiter, seconds)