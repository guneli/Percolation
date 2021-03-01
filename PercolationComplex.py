# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:53:49 2020 
@author: Gunel
"""
import decimal
import numpy as np
import csv
import collections
import gc
from os import path
labels={}
def create_Lattice(L, p): 
        for i in range(1,int((L*L)/2)):  
          labels.update({i:i})
        r = np.random.rand(L,L);
        A = np.zeros((L,L),dtype=np.int);
        for i in range(0,L):
            for j in range(0,L):
                if r[i,j] < p:
                    A[i,j] = 1;
                #otherwise it will stay empty - 0
        return A
def ALRB(i, j, A): #above left right below
    if i > 0 and j > 0:
        above = A[i-1,j];
        left = A[i,j-1];
    elif i > 0 and j == 0:
        above = A[i-1,j];
        left = 0;
    elif i == 0 and j > 0:
        above = 0;
        left = A[i,j-1];
    else:
        above = 0; 
        left = 0;
    
    if i < len(A)-1 and j < len(A)-1:
        below = A[i+1,j];
        right = A[i,j+1];
    elif i <len(A)-1 and j == len(A)-1:
        below = A[i+1,j];
        right = 0;
    elif i == len(A)-1 and j <len(A)-1:
        below = 0;
        right = A[i,j+1];
    else:
        below = 0; 
        right = 0;
    return (above,left,below,right)
#Burning Algorithm
def shortest_Path(A):
    t=2
    f=True
 
    for i in range(0,len(A)):
        if(A[0,i]==1):
            A[0,i]=t     
    while(f):
        f=False
        k=t+1
        for i in range(0,len(A)):
            for j in range(0,len(A)):        
                if(A[i,j]==t):
                     f=True         
                     l_a = ALRB(i,j,A)
                     above = l_a[0]
                     left  = l_a[1]
                     below = l_a[2]
                     right = l_a[3]
                     if(left==1):
                         A[i,j-1]=k
                         
                     if(right==1):
                         A[i,j+1]=k
                         
                     if(above==1):
                         A[i-1,j]=k
                         
                     if(below==1): 
                         A[i+1,j]=k 
                     if(i==len(A)-1):                        
                         return t-1  
        t=t+1
    return 0
#Hoshen-Kopelman Algorithm
def distribution_Clusters(A): 
    k = 1;  #cluster label
    M_k={} #the number of sites belonging to a given cluster k 
    M_k.update({2:1})
    f=False
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if A[i,j]:
                f=True
                alrb = ALRB(i,j,A);
                above = alrb[0];
                left  = alrb[1];
                
                if left == 0 and above == 0:
                    k = k + 1;
                    A[i,j] = k;
                    M_k.update({k:1})
                
                elif left != 0 and above == 0:
                   
                   A[i,j] =  find(left);
                   a=A[i,j]
                   M_k.update({a:M_k[a]+1})
                elif left == 0 and above != 0:                
                  
                   A[i,j] =  find(above);
                   a=A[i,j]
                   M_k.update({a:M_k[a]+1})
                elif left == above:                
                   
                   A[i,j] = find(above);
                   a=A[i,j]
                   M_k.update({a:M_k[a]+1})
                 
                else: 
                    union(left,above);
                    a=find(above)
                    A[i,j] = a;
                    # finding elements whose parents equals a and reassigning   to  a
                    for p in range(0,i+1):  
                      for q in range(0,len(A)):
                          index=A[p,q]
                          if index!=0 and (labels[index]==left or index== left):
                              A[p,q]=a
                              M_k.update({a:M_k[a]+1})
                              M_k.update({index:-a})
                        
                    M_k.update({a:M_k[a]+1})            
    distr_Clstr={}
    for i in range(2,k+1):
        if(M_k[i]>0):
            distr_Clstr.update({M_k[i]:0})
    for i in range(2,k+1):
        if(M_k[i]>0):
            temp=M_k[i]
            distr_Clstr.update({temp:distr_Clstr[temp]+1})
    if f:
        max_ClusterSize=max(distr_Clstr)
        ClusterAve=sum(distr_Clstr)/len(distr_Clstr) 
    else:
        max_ClusterSize=0
        ClusterAve=0
    return max_ClusterSize, ClusterAve,distr_Clstr

def union( x, y):
    labels[find(x)] = find(y);
    
def find(x):
    y = x;
    while (labels[y] != y):
        y = labels[y];
    while (labels[x] != x) : 
        z = labels[x];
        labels[x] = y;
        x = z;
    return y;
       
def writeToFile(p,Pflow,d_Min,Smax,Save,L,T):
    fileName ="Ave_L_{}_T_{}".format(L,T)
  
    if path.exists('Ave/'+fileName+'.csv'):
        
      with open('Ave/'+fileName+'.csv', 'a+', newline='') as file:
        fieldnames = ['p','Pflow', 'dMin','Smax','Save']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'p':p,'Pflow': Pflow, 'dMin': d_Min,'Smax':Smax,'Save':Save})
    else:
        with open('Ave/'+fileName+'.csv', 'w', newline='') as file:
            fieldnames = ['p','Pflow', 'dMin','Smax','Save']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'p':p,'Pflow': Pflow, 'dMin': d_Min,'Smax':Smax,'Save':Save})
    file.close()
def writeDistrToFile(P,L,T,distr_Clstr):
    od = collections.OrderedDict(sorted(distr_Clstr.items())) 
    fileName ="Dist_p_{}_L_{}_T_{}".format(P,L,T)
    with open('Dist/'+fileName+'.csv', 'w', newline='') as file:
        fieldnames = ['s','n(s,p,L)']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i,j in od.items():
          writer.writerow({'s':i,'n(s,p,L)':j})
    file.close()

def main(): 
    
    with open('perc_ini.csv', newline='') as file:
        reader = csv.DictReader(file,)
        for row in reader:
            L=int(row['L'])
            T=int(row['T'])
            p0=decimal.Decimal(row['p0'])
            pk=int(row['pk'])
            dp=decimal.Decimal(row['dp'])    
    file.close()
    p=p0
    while p<=pk:
        print(p)
        sum1=0
        sum2=0
        sum3=0
        dm=0
        d=0
        cs=0
        ca=0
        AveDMin=0
        Pflow=0
        AveofClsSizeAve=0
        AveofMaxCls=0
        distr_Clstr_Ave={}
        for t in range(1,T+1):
            Lattice=create_Lattice(L,p)
            d_Min=shortest_Path(Lattice.copy())
            list_val=distribution_Clusters(Lattice.copy())
            max_ClusterSize=list_val[0]
            ClusterAve=list_val[1]
            distr_Clstr=list_val[2]
            if(max_ClusterSize!=0):
              sum1=sum1+max_ClusterSize
              cs=cs+1
            if(ClusterAve!=0):
              sum2=sum2+ClusterAve
              ca=ca+1
            if(d_Min!=0): 
                sum3=sum3+d_Min
                dm=dm+1
            else:
                 d=d+1
            for i in distr_Clstr:
               if(i in  distr_Clstr_Ave):
                    distr_Clstr_Ave.update({i:distr_Clstr_Ave[i]+distr_Clstr[i]})
               else:
                 distr_Clstr_Ave.update({i:distr_Clstr[i]})

        if(ca!=0):  
          AveofClsSizeAve=sum2/ca    
        if(cs!=0):
            AveofMaxCls=sum1/cs
        if(dm!=0):
            AveDMin=sum3/dm
            Pflow=dm/T  
        for i in distr_Clstr_Ave:
           distr_Clstr_Ave.update({i:distr_Clstr_Ave[i]/T})
        writeToFile(p,Pflow,AveDMin,AveofMaxCls,AveofClsSizeAve,L,T)
        writeDistrToFile(p,L,T,distr_Clstr_Ave)
        gc.collect()
        p=p+dp         
main()