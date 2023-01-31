import os
from datetime import datetime
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("inputFiles", nargs="+")
parser.add_argument("-o", "--output")

args = parser.parse_args()

output = open(args.output, "w")
output.write("/*********************************************************************\n")
output.write("*\n")
output.write("*\tfile: %s\n" % os.path.basename(args.output))
output.write("*\tnote: string literals auto-generated by embed_text.py\n")
output.write("*\tdate: %s\n" % datetime.now().strftime("%d/%m%Y"))
output.write("*\n")
output.write("**********************************************************************/\n")

outSymbol = (os.path.splitext(os.path.basename(args.output))[0]).upper()

output.write("#ifndef __%s_H__\n" % outSymbol)
output.write("#define __%s_H__\n" % outSymbol)
output.write("\n\n")

for fileName in args.inputFiles:
	f = open(fileName, "r")
	lines = f.read().splitlines()

	output.write("//NOTE: string imported from %s\n" % fileName)

	stringName = os.path.splitext(os.path.basename(fileName))[0]
	output.write("const char* %s = " % stringName)

	for line in lines:
		output.write("\n\"%s\\n\"" % line)

	output.write(";\n\n")
	f.close()

output.write("#endif // __%s_H__\n" % outSymbol)

output.close()
