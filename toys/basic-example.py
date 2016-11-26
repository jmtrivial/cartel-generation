#!/usr/bin/python

import svgwrite


dwg = svgwrite.Drawing(filename = "example.svg", size = ("20cm", "15cm"))

dwg.add(dwg.image("../img/vermont_bg_big.png", insert = ("0px", "0px"), size = ("20cm", "15cm")))
		
dwg.save()
