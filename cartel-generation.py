#!/usr/bin/python

import csv
import sys
import getopt

def help():
    print 'cartel-generation.py -c <input-csv-file> -o <output-svg-file>'

def main(argv):
    inputcsvfile = ''
    outputsvgfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["icsv=","osvg="])
    except getopt.GetoptError:
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
        print "You have to give input and output parameters"
        print " "
        help()
        sys.exit(3)

    print 'Input csv file is "'+inputcsvfile+'"'
    print 'Output svg file is "'+outputsvgfile+'"'

if __name__ == "__main__":
    main(sys.argv[1:])
