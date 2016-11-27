#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import getopt
import array

import xml.etree.cElementTree as ET


# from abc import ABCMeta



# class CartelTemplate:
#     __metaclass__ = ABCMeta

#     @abstractmethod
#     def width: raise NotImplementedError

#     @abstractmethod
#     def height: raise NotImplementedError


# class BaseCartelDescription:
#     __metaclass__ = ABCMeta

#     @abstractmethod
#     def render(self, template): raise NotImplementedError





avenirStyle = "font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;line-height:125%;font-family:Avenir;-inkscape-font-specification:'Avenir, Medium';text-align:start;writing-mode:lr-tb;"
avenirStyleLeft = avenirStyle+"text-anchor:start;"
avenirStyleRight = avenirStyle+"text-anchor:end;"

format_config = {
	"1": {"w":20, "h":15},
	"2": {"w":10, "h":6}
}
unit = "cm"



class CartelContent:
	def __init__(self, author, title, date, description, technique, collection, template):

		self._template = template
		self._author = author
		self._title = title
		self._date = date
		self._description = description
		self._technique = technique
		self._collection = collection

	def size(self): 
		return format_config[self._template]

	def widthWithUnit(self):
		return str(format_config[self._template]["w"]) + unit

	def heightWithUnit(self):
		return str(format_config[self._template]["h"]) + unit

	# def render(self, x ,y):
	# 	if(self._template == "1"):
	# 		print "render 2"
	# 	elif(self._template == "2"):
	# 		print "render 2"
		

	def render(self, rootXML, x, y):
		cartel = ET.SubElement(rootXML, "svg",  {"height":self.heightWithUnit(), "width":self.widthWithUnit(), "x":str(x)+unit, "y":str(y)+unit})
		image = ET.SubElement(cartel, "image", {"height":self.heightWithUnit(), "width":self.widthWithUnit(), "x":"0cm", "y":"0cm", "xlink:href":"img/vermont_bg_big.png"})

		author = ET.SubElement(cartel, "text", {"style":avenirStyleLeft + "font-size:22px", "x":"2cm", "y":"2cm"}).text = self._author.decode('utf-8')

		titleBox =  ET.SubElement(cartel, "flowRoot")
		titleBoxRegion = ET.SubElement(titleBox, "flowRegion")
		titleBoxRegionShape =  ET.SubElement(titleBoxRegion, "rect", {"width":"17cm", "height":"4cm", "x":"2cm", "y":"2.8cm"})
		title = ET.SubElement(titleBox, "flowPara", { "style":avenirStyleLeft + "font-size:40px" }).text = self._title.decode('utf-8')
		date = ET.SubElement(titleBox, "flowPara", { "style":avenirStyleLeft + "font-size:23px" }).text = self._date.decode('utf-8')

		descBox =  ET.SubElement(cartel, "flowRoot")
		descBoxRegion = ET.SubElement(descBox, "flowRegion")
		descBoxRegionShape =  ET.SubElement(descBoxRegion, "rect", {"width":"17cm", "height":"5.5cm", "x":"2cm", "y":"7.5cm"})
		text = ET.SubElement(descBox, "flowPara", { "style":avenirStyleLeft + "font-size:21px" }).text = self._description.decode('utf-8')

		media = ET.SubElement(cartel, "text", {"style":avenirStyleLeft + "font-size:22px", "x":"2cm", "y":"13.5cm"}).text = self._technique.decode('utf-8')

		collection = ET.SubElement(cartel, "text", {"style":avenirStyleRight + "font-size:22px", "x":"19cm", "y":"13.5cm"}).text = self._collection.decode('utf-8')

		cornerTopLeft = ET.SubElement(cartel, "path", {"style":"fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1", "d":"M 20 0 L 0 0 L 0 20"})




class FinalDocument:
	def __init__(self, documents, width = 100, unit = "cm"):
		self._documents = documents
		self._width = width
		
		self._x = 0
		self._y = 0

		self.initSVG()


	# compute document limits	
	def initSVG(self):
		x = 0
		y = 0

		for document in filter(lambda x : x._template == "1", self._documents):
			if(x + document.size()["w"] > self._width):
				# goto new line
				y += document.size()["h"]
				# reset x origin
				x = 0
				x += document.size()["w"]
			else:
				x += document.size()["w"]
			
				
		
		# go to nex line
		if(x != 0):
			y += format_config["1"]["h"]
			x = 0


		for document in filter(lambda x : x._template == "1", self._documents):
			if(x + document.size()["w"] > self._width):
				# goto new line
				y += document.size()["h"]
				# reset x origin
				x = 0
				x += document.size()["w"]
			else:
				x += document.size()["w"]

		self._svgContainer = ET.Element("svg", {"version":"1.2", "xmlns:xlink":"http://www.w3.org/1999/xlink", "xmlns":"http://www.w3.org/2000/svg", "height":str(y)+unit, "width":str(self._width)+unit})
		
		colorProfileDef = ET.SubElement(self._svgContainer, "defs")
		colorProfile = ET.SubElement(colorProfileDef, "color-profile", { "name":"FOGRA39L-Coated", "xlink:href":"/usr/share/color/icc/colord/FOGRA39L_coated.icc" })




	# render global document
	def render(self, filePath = "document.svg"):
		# insert first template
		for document in filter(lambda x : x._template == "1", self._documents):
			if(self._x + document.size()["w"] > self._width):
				# goto new line
				self._y += document.size()["h"]
				# reset x origin
				self._x = 0
				document.render(self._svgContainer, self._x, self._y)
				#  
				self._x += document.size()["w"]
			else:
				document.render(self._svgContainer, self._x, self._y)
				self._x += document.size()["w"]
			
		
		# go to nex line
		if(self._x != 0):
			self._y += format_config["1"]["h"]
		

		# insert other template
		for document in filter(lambda x : x._template == "2", self._documents):
			if(self._x + document.size()["w"] > self._width):
				# goto new line
				self._y += document.size()["h"]
				# reset x origin
				self._x = 0
				document.render(self._svgContainer, self._x, self._y)
				#  
				self._x += document.size()["w"]
			else:
				document.render(self._svgContainer, self._x, self._y)
				self._x += document.size()["w"]
			

		tree = ET.ElementTree(self._svgContainer)
		tree.write(filePath)








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
	row = ["Roget Jourdain  (1845-1918)", "Élection du Conseil municipal, tableau récapitulatif des votes", "19ème siècle", "Lorem ipsum dolor sit amet, consectetur adi", "Aquarelle   29,5 x 49,5 cm", "Musée d'histoire locale", "1"]
	l = []
	auteur, titre, date, description, technique, collection, template = row
	l.append(CartelContent(auteur, titre, date, description, technique, collection, template))
	l.append(CartelContent(auteur, titre, date, description, technique, collection, template))
	l.append(CartelContent(auteur, titre, date, description, technique, collection, template))
	l.append(CartelContent(auteur, titre, date, description, technique, collection, template))
	l.append(CartelContent(auteur, titre, date, description, technique, collection, template))
	l.append(CartelContent(auteur, titre, date, description, technique, collection, template))

	doc = FinalDocument(l)
	doc.render()


	# inputcsvfile = ''
	# outputsvgfile = ''
	# try:
	# 	opts, args = getopt.getopt(argv,"hi:o:",["icsv=","osvg="])
	# except getopt.GetoptError:
	# 	print "Error while reading parameters. Abort."
	# 	help()
	# 	sys.exit(2)
	# for opt, arg in opts:
	# 	if opt == '-h':
	# 		help()
	# 		sys.exit()
	# 	elif opt in ("-i", "--icsv"):
	# 		inputcsvfile = arg
	# 	elif opt in ("-o", "--osvg"):
	# 		outputsvgfile = arg

	# if outputsvgfile == "" or inputcsvfile == "":
	# 	print "You have to give input and output parameters."
	# 	print " "
	# 	help()
	# 	sys.exit(3)

	# print 'Loading input csv file "'+inputcsvfile+'"'
	# try:
	# 	cartelDescriptions = loadCartelDescriptions(inputcsvfile)

	# except:
	# 	print "Error while reading csv file. Abort."
	# 	sys.exit(4)
	
	# print "Initialize final document"
	# finalDocument = FinalDocument(cartelDescriptions)

	# print 'Save final document as "'+outputsvgfile+'"'
	# finalDocument.generate(outputsvgfile)
	
	


if __name__ == "__main__":
	main(sys.argv[1:])
