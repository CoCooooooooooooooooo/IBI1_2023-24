import os
os.getcwd()
# change the repo
os.chdir("/Users/86136/Downloads")
os.getcwd()
# use with to open the file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as xfile:
    # read and divide the content of the file
    lines = xfile.read().split('\n')
    
    # create a dictionary to store the file
    dic={}
    # pass through the lines in the file
    for line in lines:
      if line.startswith(">"):
        name=line
        dic[name]=""
      else:
        dic[name]+=line.replace("\n","")


    # create a list called duplication
    duplication = {}
    # pass through the lines in the file
    for i in dic:
        if "duplication" in i:
            name=i.split()[0]
            duplication[name]=dic[i] 
# initialize a string to save the output 
output = ""
# go through the content of duplication
for key, value in duplication.items():  
    # check if is start with ">" 
    if key.startswith('>'):  
        # add  line break if there is a ">"
        output += f"\n{key}: {value}\n"  
    else:   
        output += f"{key}: {value} "  
print(output.strip())
output_file=open("duplicate_genes.fa","w") 
        