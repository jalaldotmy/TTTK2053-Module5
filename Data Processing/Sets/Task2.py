#Task 2 : Based on the following script, elaborate the purpose of set-theoretic methods
def main():
    ## Demonstrate set-theoretic methods.
    # Use the two files to create two sets.
    infile = open("File1.txt", 'r')
    firstSet = {line.rstrip() + "\n" for line in infile}
    infile.close()
    
    infile = open("File2.txt", 'r')
    secondSet = {line.rstrip() + "\n" for line in infile}
    infile.close()
    # Create files containing the union, intersection, and difference of
    # the original two files.
    outfile = open("Union.txt", 'w')
    outfile.writelines(firstSet.union(secondSet))
    outfile.close()
    outfile = open("Intersection.txt", 'w')
    outfile.writelines(firstSet.intersection(secondSet))
    outfile.close()
    outfile = open("Difference.txt", 'w')
    outfile.writelines(firstSet.difference(secondSet))
    outfile.close()

main()
