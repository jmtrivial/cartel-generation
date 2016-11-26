#!/usr/bin/python

import csv
import sys
import getopt

class Cartel:
	def __init__(self, row):
		pass

def loadCartelDescriptions(csvfile):
	result = list()
	with open(csvfile, 'rb') as csvcontent:
		spamreader = csv.reader(csvcontent, delimiter=' ', quotechar='|')
		for row in spamreader:
			result.append(Cartel(row)) 
	return result

def help():
	print 'cartel-generation.py -c <input-csv-file> -o <output-svg-file>'

def main(argv):
	inputcsvfile = ''
	outputsvgfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["icsv=","osvg="])
	except getopt.GetoptError:
		print "Error while reading parameters. Abort."
		help()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			help()
			sys.exit()
		elif opt in ("-i", "--icsv"):
			inputcsvfile = arg
		elif opt in ("-o", "--osvg"):
			outputsvgfile = arg

	if outputsvgfile == "" or inputcsvfile == "":
		print "You have to give input and output parameters."
		print " "
		help()
		sys.exit(3)

	print 'Loading input csv file "'+inputcsvfile+'"'
	try:
		cartelDescriptions = loadCartelDescriptions(inputcsvfile)
	except:
		print "Error while reading csv file. Abort."
		sys.exit(4)
	
	print 'Output svg file is "'+outputsvgfile+'"'


if __name__ == "__main__":
	main(sys.argv[1:])
