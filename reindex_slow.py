# /*
#  * @Author: Ron.Hu
#  * @Date: 2022-08-12 16:25:37 
#  * @Last Modified by:   Ron.Hu
#  * @Last Modified time: 2022-08-12 16:25:37 
#  */

import sys
from operator import itemgetter
import numpy as np
import time

read_file=sys.argv[1]
# write_file=sys.argv[2]

#read the file
max_id=0
f=open(read_file,"r")
line=f.read()
line=line[:-1]   #get elemnts except the last one
line=line.split("\n")  #split the string line by space "Line1-abcdef \nLine2-abc \nLine4-abcd"


#input: fromNodeID toNodeID weight timestamp
#output: fromNodeID  toNodeID
#        toNodeID  fromNodeID
#re-index node-id
time_start=time.time()
new_id=[]
for i in range(len(line)):
    row=line[i].split()
    
    start=int(row[0])
    end=int(row[1])
    
    #re-index start point
    try:
        start_find=new_id.index(start)
        start_idx=int(start_find)
    except:
        new_id.append(start)
        start_idx=len(new_id)-1
    
    #re-index end point
    try:
        end_find=new_id.index(end)
        end_idx=int(end_find)
    except:
        new_id.append(end)
        end_idx=len(new_id)-1
    # row=[start_idx,end_idx]

    
    # append valid edge to data[]
    # row=str(row[0])+' '+str(row[1])+'\n'       #node id start from 0
    # if i%10000==0:
    #     print(row)
    # data.append(row)


time_end=time.time()
print('time cost: ',time_end-time_start,' s')

# with open(write_file,"w") as f:
#     #f.writelines(firstLine)
#     for i in data:
#         f.writelines(i)

# print("finished generating: ", write_file) 
# print("original edge number: ", len(line)) 
# print("generated edge number: ", len(data)) 

