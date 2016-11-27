#!/usr/bin/python
# -*- coding: utf-8 -*-

import svgwrite

avenirStyle = "font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;line-height:125%;font-family:Avenir;-inkscape-font-specification:'Avenir, Medium';text-align:start;writing-mode:lr-tb;text-anchor:start;"

dwg = svgwrite.Drawing(filename = "example.svg", size = ("20cm", "15cm"))

dwg.add(dwg.image("../img/vermont_bg_big.png", insert = ("0cm", "0cm"), size = ("20cm", "15cm")))

dwg.add(dwg.text("Roget Jourdain  (1845-1918)", insert = ("2cm", "2cm"), style = avenirStyle + "font-size:21.84086609px"))

#title = dwg.tspan("Élection du Conseil municipal, tableau récapitulatif des votes", style = avenirStyle + "font-size:47.67940903px")
#date = dwg.tspan("19ème siècle", style = avenirStyle + "font-size:23.15856925px")
#titleDateArea = dwg.textArea(insert = ("70", "113"), size= ("668", "166"))
#titleDateArea.add(title)
#titleDateArea.add(date)
#dwg.add(titleDateArea)
dwg.save()
