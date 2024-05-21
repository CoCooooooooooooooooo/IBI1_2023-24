# define a function to receive file informationn
def DNA_sequence(file):
    seq=""
    # use for to go through the fasta file(except for the 1st line)
    for i in range(1,len(file)):
        seq+=file[i].replace("\n","")
    return seq
file1=open("SLC6A4_HUMAN.fa",'rt')
file_human=file1.read().split("\n")
file_human1=DNA_sequence(file_human)
file2=open("SLC6A4_MOUSE.fa","rt")
file_mouse=file2.read().split("\n")
file_mouse1=DNA_sequence(file_mouse)
file3=open("SLC6A4_RAT.fa","rt")
file_rat=file3.read().split("\n")      
file_rat1=DNA_sequence(file_rat)
matrix=open("IBI.txt","rt")
matrix=matrix.read().split("\n")

matrix1=[]
for i in matrix:
    i=i.split()
    matrix1.append(i)
BLOSUM62={}

for i in matrix1[0]:
    BLOSUM62[i]={}
for i in range(1,len(matrix1)):
    key=matrix1[i][0]
    for j in range(1,len(matrix1[i])):
        BLOSUM62[matrix1[0][j-1]][key]=matrix1[i][j]
# define a functio to compare the 
def comparison(file1,file2):
    score=0
    len1=min(len(file1),len(file2))
    for i in range(len1):
        for j in BLOSUM62.keys():
            if j==file1[i]:
                for z in BLOSUM62[j].keys():
                    if z==file2[i]:
                        score+=int(BLOSUM62[j][z])
    return score

def identical(file1,file2):
    num=0
    len1=min(len(file1),len(file2))
    for i in range(len1):
        if file1[i]==file2[i]:
            num+=1
    percent=str(num/len1*100)+"%"
    return percent

human_mouse_1=comparison(file_human1,file_mouse1)
human_rat_1=comparison(file_human1,file_rat1)
mouse_rat_1=comparison(file_mouse1,file_rat1)
print("The alignment score between human's sequence and mouse's sequence is",human_mouse_1)
print("The alignment score between human's sequence and rat's sequence is",human_rat_1)
print("The alignment score between rat's sequence and mouse's sequence is",mouse_rat_1)

human_mouse2=identical(file_human1,file_mouse1)
human_rat2=identical(file_human1,file_rat1)
mouse_rat2=identical(file_mouse1,file_rat1)
# print the result
print("The percentage of identical amino acid between human's sequence and mouse's sequence is",human_mouse2)
print("The percentage of identical amino acid between human's sequence and mouse's sequence is",human_rat2)
print("The percentage of identical amino acid between human's sequence and mouse's sequence is",mouse_rat2)

# determine which	of the	two	species’ sequences are	most closely related
if human_mouse_1>human_rat_1 and human_mouse_1>mouse_rat_1:
    print("Human's sequence and mouse's sequence are most closely ralated")
elif human_rat_1>human_mouse_1 and human_rat_1>mouse_rat_1:
    print("Human's sequence and rat's sequence are most closely ralated")
else:
    print("Rat's sequence and mouse's sequence are most closely ralated")
#determine which gene is more similar to human gene to know which species is better for model organism      
if human_mouse_1>human_rat_1:
    print("Mouse is a better model organism for human based on the data analysed here.")
elif human_mouse_1<human_rat_1:
    print("Rat is a	better model organism for human based on the data analysed here.")



    
    
    