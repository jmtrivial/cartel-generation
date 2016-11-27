#!/usr/bin/python

import svgwrite


dwg = svgwrite.Drawing(filename = "example.svg", size = ("20cm", "15cm"))

dwg.add(dwg.image("../img/vermont_bg_big.png", insert = ("0cm", "0cm"), size = ("20cm", "15cm")))
name = dwg.text("Roget Jourdain  (1845-1918)", insert = ("66", "77"), style = "font-style:normal;font-weight:normal;font-size:21.84115791px;line-height:125%;font-family:sans-serif;text-align:start;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1")
dwg.add(name)


dwg.save()
