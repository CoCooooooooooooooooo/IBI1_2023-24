import os
import re
os.getcwd()
sequence=input("please input one of tworepetitive sequence(GTGTGT Or GTCTGT):")
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
input_file = file.read().split(sep='\n')
output_file=open(sequence+"duplicate_genes.fa","w") 
#create a new file
firstfile={} #create a dictionary to store DNA name and sequence
for line in input_file:
    if line.startswith(">"):
        name=line
        firstfile[name]=""
    else:
        firstfile[name]+=line.replace("\n","")

#create a dictionary to store deplicated genes' names and sequences
xfile={}
for i in firstfile.keys():
    if "duplication" in i and sequence in firstfile[i]:
        seq=str(firstfile[i])
        num=seq.count(sequence)
        name=i.split()[0]
        xfile[name]=firstfile[i]
for i in xfile.keys():#write new file
    output_file.write(i)
output_file.write("\n")
output_file.write(xfile[i])
output_file.write("\n")
file.close()