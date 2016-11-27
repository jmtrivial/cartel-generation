#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET


avenirStyle = "font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;line-height:125%;font-family:Avenir;-inkscape-font-specification:'Avenir, Medium';text-align:start;writing-mode:lr-tb;"
avenirStyleLeft = avenirStyle+"text-anchor:start;"
avenirStyleRight = avenirStyle+"text-anchor:end;"


def addCartel(root, x, y, txtAuthor, txtTitle, txtDate, txtText, txtMedia, txtCollection):
	cartel = ET.SubElement(root, "svg",  {"height":"15cm", "width":"20cm", "x":x, "y":y})
	image = ET.SubElement(cartel, "image", {"height":"15cm", "width":"20cm", "x":"0cm", "y":"0cm", "xlink:href":"../img/vermont_bg_big.png"})

	author = ET.SubElement(cartel, "text", {"style":avenirStyleLeft + "font-size:22px", "x":"2cm", "y":"2cm"}).text = txtAuthor.decode('utf-8')

	titleBox =  ET.SubElement(cartel, "flowRoot")
	titleBoxRegion = ET.SubElement(titleBox, "flowRegion")
	titleBoxRegionShape =  ET.SubElement(titleBoxRegion, "rect", {"width":"17cm", "height":"4cm", "x":"2cm", "y":"2.8cm"})
	title = ET.SubElement(titleBox, "flowPara", { "style":avenirStyleLeft + "font-size:40px" }).text = txtTitle.decode('utf-8')
	date = ET.SubElement(titleBox, "flowPara", { "style":avenirStyleLeft + "font-size:23px" }).text = txtDate.decode('utf-8')

	descBox =  ET.SubElement(cartel, "flowRoot")
	descBoxRegion = ET.SubElement(descBox, "flowRegion")
	descBoxRegionShape =  ET.SubElement(descBoxRegion, "rect", {"width":"17cm", "height":"5.5cm", "x":"2cm", "y":"7.5cm"})
	text = ET.SubElement(descBox, "flowPara", { "style":avenirStyleLeft + "font-size:21px" }).text = txtText.decode('utf-8')

	media = ET.SubElement(cartel, "text", {"style":avenirStyleLeft + "font-size:22px", "x":"2cm", "y":"13.5cm"}).text = txtMedia.decode('utf-8')

	collection = ET.SubElement(cartel, "text", {"style":avenirStyleRight + "font-size:22px", "x":"19cm", "y":"13.5cm"}).text = txtCollection.decode('utf-8')



root = ET.Element("svg", {"version":"1.1", "xmlns:xlink":"http://www.w3.org/1999/xlink", "xmlns":"http://www.w3.org/2000/svg", "height":"30cm", "width":"40cm"})

addCartel(root, "0cm", "0cm", "Roget Jourdain  (1845-1918)", "Élection du Conseil municipal, tableau récapitulatif des votes", "19ème siècle", "Lorem ipsum dolor sit amet, consectetur adi", "Aquarelle   29,5 x 49,5 cm", "Musée d'histoire locale")
addCartel(root, "20cm", "0cm", "Roget Jourdain  (1845-1918)", "Élection du Conseil municipal, tableau récapitulatif des votes", "19ème siècle", "Lorem ipsum dolor sit amet, consectetur adi", "Aquarelle   29,5 x 49,5 cm", "Musée d'histoire locale")
addCartel(root, "0cm", "15cm", "Roget Jourdain  (1845-1918)", "Élection du Conseil municipal, tableau récapitulatif des votes", "19ème siècle", "Lorem ipsum dolor sit amet, consectetur adi", "Aquarelle   29,5 x 49,5 cm", "Musée d'histoire locale")
addCartel(root, "20cm", "15cm", "Roget Jourdain  (1845-1918)", "Élection du Conseil municipal, tableau récapitulatif des votes", "19ème siècle", "Lorem ipsum dolor sit amet, consectetur adi", "Aquarelle   29,5 x 49,5 cm", "Musée d'histoire locale")


tree = ET.ElementTree(root)
tree.write("example.svg")
