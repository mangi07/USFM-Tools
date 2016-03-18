# Copyright (c) 2016 unfoldingWord
#  http://creativecommons.org/licenses/MIT/
#  See LICENSE file for details.
#
#  Contributors:
#  Ben Olson <mangi07@users.noreply.github.com>
#
#  Intended to combine USFM content from all *.txt files
#  in script's directory and subdirectories into a new
#  file identified by the user:
#  
#  Usage:  python USFM2book.py <destination file>


import fnmatch
import os
import re
import sys
import pdb


def parseFile(sourceFile):
	fileString = '\n'
	with open(sourceFile, 'rU') as f:
		for line in f:
			"""Add newline between all verses..."""
			tempString = re.sub(r'\\v', r'\n\\v', line)
			tempString = re.sub(r'^\n\\v', r'\\v', tempString)
			fileString += tempString
			"""...OR use sourceFile content as is:"""
			# tempString += line
	fileString += '\n'
	return fileString


def getDestFile():
	if len(sys.argv) < 2:
		print "Usage: python USFM2book.py <destination file>"
		sys.exit()
	return sys.argv[1]


# pdb.set_trace()

destString = ''
destFile = getDestFile()


for root, dirs, files in os.walk('.'):
	for filename in files:
		if fnmatch.fnmatch(filename, '*.txt'):
			sourceFile = os.path.join(root, filename)
			destString += parseFile(sourceFile)

# print destString

if not os.path.exists(destFile):
	destinationFile = open(destFile, 'w')
	destinationFile.write(destString)
	destinationFile.close()
else:
	print "Write failed. " + destFile + " already exists."

