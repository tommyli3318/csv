import csv
import re

out_f = open('output.csv', "w")

with open('file.csv') as file:
	page = csv.reader(file)
	for row in page:
		# look for date in row[0]
		result = re.search('\d*\/\d*', row[0]) # match the date
		line = result.group(0) if result else ''
		out_f.write(line + '\n')