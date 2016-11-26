#!/usr/bin/python

import csv
import sys
import getopt
import array

class Cartel:
	def __init__(self, row):
		# TODO: set self._size as "large" or "small"
		self._size = "large"
		# TODO set other self._...
		pass
	def getSize(self):
		return self._size

class Format:
	def __init(self, width, height):
		self._width = width
		self._height = height
	def setNbCartels(self, number):
		self._number = number

class FinalDocument:
	
	def __init__(self, cartelDescriptions):
		self._format = {}
		self.addFormat("large", 20, 15)
		self.addFormat("small", 10, 6)
		self.initStructure(cartelDescriptions)
		pass
	
	def addFormat(self, formatName, width, height):
		self._format[formatName] = Cartel(width, height)
		
	def initStructure(self, cartelDescriptions):
		self._cartels = {}
		for f in self._formats:
			self._cartels[f.name] = []
		for desc in cartelDescriptions:
			cartelSize = desc.getSize()
			if cartelSize in self._format:
				self._cartels[cartelSize] = desc
			else:
				print "Unknown cartel format"
			
	def generate(self, svgfile):
		computeLayout()
		# TODO
		pass
	def computeLayout(self):
		# TODO: for each format, get the number of corresponding cartels
		# compute the number of cartels per line
		# then compute the number of required lines
		# then deduce the required height
		
		# TODO: then deduce the size of the final document
		self._documentWidth = 100
		# self._documentHeight = 
		

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
	
	print "Initialize final document"
	finalDocument = FinalDocument(cartelDescriptions)

	print 'Save final document as "'+outputsvgfile+'"'
	finalDocument.generate(outputsvgfile)
	
	


if __name__ == "__main__":
	main(sys.argv[1:])
