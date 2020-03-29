from numpy import *
from matplotlib.pyplot import*
from random import *
import time
def tab():
    tab=[]
    tab2=[]
    size=randint(2,10)
    for i in range(size):
        tab.append(randint(-9,9))
    return tab
def bucket(tab):
    clock_start = time.perf_counter()
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
    clock_stop = time.perf_counter()
    print("time",(clock_stop-clock_start)/0.10)
    return mal

def bubble(tab):
    clock_start = time.perf_counter()
    r1=tab.copy()
    s = len(r1)
    for i in range(s):
        for j in range(0, s-i-1):
            if r1[j] > r1[j+1] :
                r1[j], r1[j+1] = r1[j+1], r1[j]
    clock_stop = time.perf_counter()
    print("time",(clock_stop-clock_start)/0.10)
    return r1
def val(tab,p):
    t=tab
    t1=[]
    t2=[]
    t4a=[]
    t4b=[]
    p=p
    w=0
    e=0
    while (w<3) and (e<len(t)):
        if (t[e]>p):
            w=w+1
            t1.append(t[e])
            t2.append(e)
        e=e+1
    buc=bucket(t1)
    bub=bubble(t1)
    bub.reverse()
    for i in range(3):
        for j in range(3):
            if (buc[i]==t1[j]):
                t4a.append(t2[j])
    for i in range(3):
        for j in range(3):
            if (bub[i]==t1[j]):
                t4b.append(t2[j])
    return t4a,t4b
