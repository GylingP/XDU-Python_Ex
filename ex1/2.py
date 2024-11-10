import random as rd
from collections import Counter
lst=[]
for i in range(0,1000):
    lst.append(rd.randint(0,100))
print(Counter(lst))