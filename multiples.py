import re
import sys

#functionality for counting the multiples of the given two numbers and the goal number
def multiple (num1, num2, goalnum):
    matchingnumbers = []
    for num in range(1, goalnum):
        if num % num1 == 0 or num % num2 == 0:
            matchingnumbers.append(str(num))
    return matchingnumbers

def main(inputfile, outputfile):
    infile = open(inputfile, "r")
    rows = []
    #read all rows of input file and perform multiple() to ones with correct input
    for line in infile:
        splittedline = line.strip().split(" ")
        numlen= len(splittedline)
        if re.match("^[0-9 ]+$", line) and numlen == 3:
            multiples = multiple(int(splittedline[0]), int(splittedline[1]), int(splittedline[2]))
            goal = splittedline[2]
            #Save values for later
            rows.append((goal, multiples))
    infile.close()
    #sort rows by ascending order of how many multiples certain row has
    rows.sort(key=lambda row: len(row[1]))
    outfile = open(outputfile, "w")
    #add rows to output file with wanted format
    for row in rows:
        line = row[0] + ":" + " ".join(row[1]) + "\n"
        outfile.write(line)
        print(line, end="")
    outfile.close()

main(sys.argv[1], sys.argv[2])