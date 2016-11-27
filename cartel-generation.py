#!/usr/bin/python

import csv
import sys
import getopt
import array
import svgwrite


from abc import ABCMeta

format_config = {
	"1": {"w":20, "h":15},
	"2": {"w":10, "h":6}
}

class CartelTemplate:
    __metaclass__ = ABCMeta

    @abstractmethod
    def width: raise NotImplementedError

    @abstractmethod
    def height: raise NotImplementedError


class BaseCartelDescription:
    __metaclass__ = ABCMeta

    @abstractmethod
    def render(self, template): raise NotImplementedError



class CartelContent:
	def __init__(self, auteur, titre, date, technique, dimensions, collection, template):

		self._cartelFormat = cartelFormat
		self._author = author
		self._title = title
		self._date = date
		self._desc = desc
		self._collection = collection
		self._meta = meta

	def size: 
		return format_config[self._cartelFormat]

	def render(self):

		if(self._cartelFormat === "1") {
			print "render 2"
		} else if(self._cartelFormat === "2"){
			print "render 2"
		}


class FinalDocument:
	def __init__(self, exportPath, documents, height = null, width = 100):
		self._documents = documents
		self._height = height
		self._width = width
		self._svgContainer = svgwrite.Drawing(exportPath, profile='tiny')
		self._x = 0
		self._y = 0
	

	def render(self):
		# insert first template
		for document in documents
			if document._cartelFormat === "1"
				if(self._x + document.size()["w"] > self._width) {
					# goto new line
					self._y += document.size()["h"]
					# reset x origin
					self._x = 0
					self._svgContainer.add(document.render(self._x, self._y))
					#  
					self._x += document.size()["w"]
				} else {
					self._svgContainer.add(document.render(self._x, self._y))
					self._x += document.size()["w"]
				}
		
		# go to nex line
		if(self._x != 0) {
			self._y += format_config["1"]["h"]
		}

		# insert other template
		for document in documents
			if document._cartelFormat === "2"
				if(self._x + document.size.w > self._width) {
					self._y += document.size.h
					self._x = 0
					self._svgContainer.add(document.render())
				} else {
					self._svgContainer.add(document.render())
					self._x += document.size.w
				}

		self._svgContainer.save()


def loadCartelDescriptions(csvfile):
	result = list()
	with open(csvfile, 'rb') as csvcontent:
		spamreader = csv.reader(csvcontent, delimiter=' ', quotechar='|')
		for row in spamreader:
			auteur, titre, date, technique, dimensions, collection, template = row;
			result.append(CartelContent(auteur, titre, date, technique, dimensions, collection, template)) 
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
