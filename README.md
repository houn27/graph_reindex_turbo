### Graph Re-index Turbo

This is a effecient script used to reindex vertex ids to be continuous (0/1 ~ node_num-1/node_num) for graph datset pre-processing. Besides, there is a full edition which can remove self-loops and multi-edges to gennerate a simple graph. 

According to the experiment, the Re-index Turbo method based on hashmaps is more than 200 times faster than the method based on index() function and lists. 



#### Input Format

{end point_1}  {space}  {end point 2}

e.g.

```
0  0
0  1
0  2
0  3
0  4
0  5
```



#### Output Format

same as the input format 



#### Run Command

##### Simple edition (only has re-index function)

python reindex_simple.py {input graph path} {output graph path}

e.g.

```
python reindex_simple.py slashdot_new.txt slashdot_reindex.txt
```



##### Full edition (with removing self-loops and multi-edges)

Options:

-l: remove self-loops

-m: remove multi-edges

-s: id starts from 0 (if the ids in original datasets start from 1 and you want them start from 0)



Commands:

python reindex_turbo.py -i {input graph path} -w {output graph path} -l -m -s

e.g.

```
python reindex_turbo.py -i slashdot_new.txt -w slashdot_reidnex.txt -l -m -s
```



#### Experiment Results

I have implemented a simple test on Slashdot dataset (https://snap.stanford.edu/data/soc-Slashdot0811.html) which shows the turbo methods is more than 200 times faster than the method based on index() function and lists (reindex_slow.py)

![turbo_perform](/Users/ron/Desktop/turbo_perform.png)





p.s. If you have any questions and advices, welcome to send emails to 849957572@qq.com 

