
"""
Created on Sat Mar 23 16:26:36 2019

@author: kmist
"""
import pandas as pd
train=pd.read_csv(r'C:\Users\kmist\Desktop\Sem 10\NNDL\Project\case_vote.csv',header=1)
train=train.drop(['1'],axis=1)
train.head(10)
votes=[]
val={}
#Iniitalizing keys and index location
def extract(column):
    pos=0
    for e in column:
        if e>9999: 
            val[e]=pos 
        pos=pos+1   
    return val

dkey=extract(train['1000'])
#dakey=pd.DataFrame.from_dict(dkey)


def makearray(e):
        va=[]
        start=dkey[e]+1
        f=e+1
        end=dkey[f]
        while start<=end-1:
            va.append(train["1000"][start])
            start=start+1
        return va
            
        
        
def finaldict(traincol):
    for e in traincol:
        
        if e>9999:
            c=makearray(e)
            val[e]=c
    return val

do=finaldict(train['1000'])

"""
import csv
 
dict = dkey
w = csv.writer(open("output.csv", "w"))
for key, val in dict.items():
  w.writerow([key, val])     
        
    """
    
# To create a list of lists from the dictionary values 
i=10002    
while i in range(10002,42580):
    dkey[i]=list(map(str,dkey[i]))
we=list(dkey.values())

#Fitting the association rule learning model
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
dat=we[1:50]
te_ary = te.fit_transform(dat,sparse=False)
df = pd.DataFrame(te_ary, columns=te.columns_)

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

print (frequent_itemsets)

from mlxtend.frequent_patterns import association_rules
t=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

import numpy as np
from pandas import DataFrame
import matplotlib
matplotlib.use('agg') 
import matplotlib.pyplot as plt

# Convert the input into a 2D dictionary
freqMap = {}
data=we[10:12]
for line in data:
  for item in line:
    if not item in freqMap:
      freqMap[item] = {}

    for other_item in line:
      if not other_item in freqMap:
        freqMap[other_item] = {}

      freqMap[item][other_item] = freqMap[item].get(other_item, 0) + 1
      freqMap[other_item][item] = freqMap[other_item].get(item, 0) + 1

df = DataFrame(freqMap).T.fillna(0)
print (df)

plt.pcolormesh(df, edgecolors='black')
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.savefig('plot.png')
plt.show()


