#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET

avenirStyle = "font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;line-height:125%;font-family:Avenir;-inkscape-font-specification:'Avenir, Medium';text-align:start;writing-mode:lr-tb;"
avenirStyleLeft = avenirStyle+"text-anchor:start;"
avenirStyleRight = avenirStyle+"text-anchor:end;"

root = ET.Element("svg", {"version":"1.1", "xmlns:xlink":"http://www.w3.org/1999/xlink", "xmlns":"http://www.w3.org/2000/svg", "height":"15cm", "width":"20cm"})

image = ET.SubElement(root, "image", {"height":"15cm", "width":"20cm", "x":"0", "y":"0", "xlink:href":"../img/vermont_bg_big.png"})

author = ET.SubElement(root, "text", {"style":avenirStyleLeft + "font-size:22px", "x":"2cm", "y":"2cm"}).text = "Roget Jourdain  (1845-1918)"

titleBox =  ET.SubElement(root, "flowRoot")
titleBoxRegion = ET.SubElement(titleBox, "flowRegion")
titleBoxRegionShape =  ET.SubElement(titleBoxRegion, "rect", {"width":"17cm", "height":"4cm", "x":"2cm", "y":"2.8cm"})
title = ET.SubElement(titleBox, "flowPara", { "style":avenirStyleLeft + "font-size:40px" }).text = "Élection du Conseil municipal, tableau récapitulatif des votes".decode('utf-8')
date = ET.SubElement(titleBox, "flowPara", { "style":avenirStyleLeft + "font-size:23px" }).text = "19ème siècle".decode('utf-8')

descBox =  ET.SubElement(root, "flowRoot")
descBoxRegion = ET.SubElement(descBox, "flowRegion")
descBoxRegionShape =  ET.SubElement(descBoxRegion, "rect", {"width":"17cm", "height":"5.5cm", "x":"2cm", "y":"7.5cm"})
title = ET.SubElement(descBox, "flowPara", { "style":avenirStyleLeft + "font-size:21px" }).text = "Lorem ipsum dolor sit amet, consectetur adi".decode('utf-8')

media = ET.SubElement(root, "text", {"style":avenirStyleLeft + "font-size:22px", "x":"2cm", "y":"13.5cm"}).text = "Aquarelle   29,5 x 49,5 cm".decode('utf-8')

collection = ET.SubElement(root, "text", {"style":avenirStyleRight + "font-size:22px", "x":"19cm", "y":"13.5cm"}).text = "Musée d'histoire locale".decode('utf-8')


tree = ET.ElementTree(root)
tree.write("example.svg")
