#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET

avenirStyle = "font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;line-height:125%;font-family:Avenir;-inkscape-font-specification:'Avenir, Medium';text-align:start;writing-mode:lr-tb;text-anchor:start;"

root = ET.Element("svg", {"version":"1.1", "xmlns:xlink":"http://www.w3.org/1999/xlink", "xmlns":"http://www.w3.org/2000/svg", "height":"15cm", "width":"20cm"})

image = ET.SubElement(root, "image", {"height":"15cm", "width":"20cm", "x":"0", "y":"0", "xlink:href":"../img/vermont_bg_big.png"})

author = ET.SubElement(root, "text", {"style":avenirStyle + "font-size:21.84086609px", "x":"2cm", "y":"2cm"}).text = "Roget Jourdain  (1845-1918)"


#dwg = svgwrite.Drawing(filename = "example.svg", size = ("20cm", "15cm"))

#dwg.add(dwg.image("../img/vermont_bg_big.png", insert = ("0cm", "0cm"), size = ("20cm", "15cm")))

#dwg.add(dwg.text("Roget Jourdain  (1845-1918)", insert = ("2cm", "2cm"), style = avenirStyle + "font-size:21.84086609px"))

#title = dwg.tspan("Élection du Conseil municipal, tableau récapitulatif des votes", style = avenirStyle + "font-size:47.67940903px")
#date = dwg.tspan("19ème siècle", style = avenirStyle + "font-size:23.15856925px")
#titleDateArea = dwg.textArea(insert = ("70", "113"), size= ("668", "166"))
#titleDateArea.add(title)
#titleDateArea.add(date)
#dwg.add(titleDateArea)
#dwg.save()

tree = ET.ElementTree(root)
tree.write("example.svg")
