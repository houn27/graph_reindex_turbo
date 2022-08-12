# /*
#  * @Author: Ron.Hu
#  * @Date: 2022-08-12 16:28:22 
#  * @Last Modified by:   Ron.Hu 
#  * @Last Modified time: 2022-08-12 16:28:22 
#  */


import sys
from operator import itemgetter
import numpy as np
import time

#paser for argument
read_file=sys.argv[1]
write_file=sys.argv[2]


#read the file
f=open(read_file,"r")
line=f.read()
line=line[:-1]   #get elemnts except the last one
line=line.split("\n")  #split the string line by space "Line1-abcdef \nLine2-abc \nLine4-abcd"

#check if the node index starting from 0
    

#create data array
data=''

#input: fromNodeID toNodeID weight timestamp
#output: fromNodeID  toNodeID
#        toNodeID  fromNodeID
#re-index node-id
time_start=time.time()
new_id=dict()
for i in range(len(line)):
    #line=f.readline()
    row=line[i].split()
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

    data+=str(row[0])+' '+str(row[1])+'\n'       #node id start from 0


time_end=time.time()
print('time cost: ',time_end-time_start,' s')

with open(write_file,"w") as f:
    f.write(data)

print("finished generating: ", write_file) 
print("original edge number: ", len(line)) 
print("generated edge number: ", len(data)) 