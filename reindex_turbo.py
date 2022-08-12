# /*
#  * @Author: Ron.Hu 
#  * @Date: 2022-08-12 16:28:58 Ron.Hu
#  * @Last Modified time: 2022-08-12 16:28:58 
#  */

import sys
from operator import itemgetter
import numpy as np
import time
from tqdm import tqdm

#paser for argument
read_file=""
write_file=""
no_loop=False
no_multi=False
start_0=False

i=0
while i < len(sys.argv):
    if(sys.argv[i]=="-i"):
        i+=1
        read_file=sys.argv[i]
    if(sys.argv[i]=="-w"):
        i+=1
        write_file=sys.argv[i]
    if(sys.argv[i]=="-l"):
        no_loop=True
    if(sys.argv[i]=="-m"):
        no_multi=True
    if(sys.argv[i]=="-s"):
        start_0=True
    i+=1
# write_file=sys.argv[2]

#read the file
f=open(read_file,"r")
line=f.read()
line=line[:-1]   #get elemnts except the last one
line=line.split("\n")  #split the string line by space "Line1-abcdef \nLine2-abc \nLine4-abcd"

#check if the node index starting from 0
flag=1
if start_0:
    for i in range(len(line)):
        row=line[i].split()
        if(int(row[0])==0 or int(row[1])==0):
            flag=0
            break

    

#create data array
data=[]
data_set=set()      #used for removing repeated edges


#input: fromNodeID toNodeID weight timestamp
#output: fromNodeID  toNodeID
#        toNodeID  fromNodeID
#re-index node-id
time_start=time.time()
new_id=dict()
for i in tqdm(range(len(line))):
    #line=f.readline()
    row=line[i].split()
    if(int(row[0])==int(row[1])) and no_loop:       #remove self-loop
        continue
    start=int(row[0])
    end=int(row[1])
    
    #re-index start point
    id_result=new_id.get(start)
    if(id_result!=None):
        start_idx=id_result
    else:
        new_id[start]=len(new_id)
        start_idx=len(new_id)-1

    id_result=new_id.get(end)
    if(id_result!=None):
        end_idx=id_result
    else:
        new_id[end]=len(new_id)
        end_idx=len(new_id)-1
    row=[start_idx,end_idx]

    # check for repeat edges
    if no_multi:
        if tuple(row) in data_set:
            continue
        reverse_row=[row[1],row[0]]  
        data_set.add(tuple(row))
        data_set.add(tuple(reverse_row))
    
    #append valid edge to data[]
    if start_0:
        row=str(row[0]-flag)+' '+str(row[1]-flag)+'\n'       #node id start from 0
    else:
        row=str(row[0])+' '+str(row[1])+'\n'       #node id start from 0
    # if i%10000==0:
    #     print(row)
    data.append(row)


time_end=time.time()
print('time cost: ',time_end-time_start,' s')

with open(write_file,"w") as f:
    #f.writelines(firstLine)
    for i in data:
        f.writelines(i)

print("finished generating: ", write_file) 
print("original edge number: ", len(line)) 
print("generated edge number: ", len(data)) 