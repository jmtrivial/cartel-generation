#!/usr/bin/python

import csv
import sys
import getopt

def help():
    print 'cartel-generation.py -c <input-csv-file> -o <output-svg-file>'

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hc:o:",["csv=","osvg="])
   except getopt.GetoptError:
      help()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         help()
         sys.exit()
      elif opt in ("-c", "--csv"):
         inputfile = arg
      elif opt in ("-o", "--osvg"):
         outputfile = arg
   print 'Input csv file is "', inputfile
   print 'Output svg file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
