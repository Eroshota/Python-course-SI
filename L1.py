
from numpy import *
from matplotlib.pyplot import*
from random import *
def tab():
    tab=[]
    tab2=[]
    size=randint(2,10)
    for i in range(size):
        tab.append(randint(-9,9))
    return tab
def bucket(tab):
    t1=tab
    s=len(t1)
    mx=max(t1)+1
    mi=min(t1)
    j=0
    t=0
    t2=[]
    ros=[]
    mal=[]
    for i in range (mi,mx):
        t=0
        j=1
        while (j<=s):
            if (t1[j-1]==i):
                t2.append(i)
                j=s
            j=j+1
            if (j>s):
                break
    for i in range(len(t2)):
        for j in range(len(t1)):
            if t2[i]==t1[j]:
                ros.append(t1[j])
    for k in range(len(ros)):
        mal.append(ros[len(ros)-k-1])
    return mal,ros

def bubble(tab):
    tab1=tab.copy()
    s = len(tab)
    for i in range(s):
        for j in range(0, s-i-1):
            if tab1[j] > tab1[j+1] :
                tab1[j], tab1[j+1] = tab1[j+1], tab1[j]
    return tab1
