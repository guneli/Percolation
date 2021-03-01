import matplotlib.pyplot as plt
import os.path
import numpy as np
path="C:/Users/Gunel/Desktop/Percolation/Distribution/"
#file1 for L=10 P=0.2
N2c=[]
S2c=[]    
S10=[]
N10=[]
for i in range(1,1000):
    fileName="Dist_p 0.2 L 10 T {}".format(i)
    completeName = os.path.join(path, fileName+".txt")
    file= open(completeName,"r")
    lines=file.readlines()
    for x in lines:
        S10.append(x.split(' ')[0])
        N10.append(x.split(' ')[2])
    file.close()
    S10=S10[1:]
    S10=[float(item) for item in S10]
    N10=N10[1:]
    N10=[float(item) for item in N10]
    N2c=N2c+N10
    S2c=S2c+S10
    S10[:]=[]
    N10[:]=[]

#file2 for L=10 P=0.3   
N3c=[]
S3c=[]
for i in range(1,1000):
    S10=[]
    N10=[]
    fileName="Dist_p 0.3 L 10 T {}".format(i)
    completeName = os.path.join(path, fileName+".txt")
    file= open(completeName,"r")
    lines=file.readlines()
    for x in lines:
        S10.append(x.split(' ')[0])
        N10.append(x.split(' ')[2])
    file.close()
    S10=S10[1:]
    S10=[float(item) for item in S10]
    N10=N10[1:]
    N10=[float(item) for item in N10]
    N3c=N3c+N10
    S3c=S3c+S10
    S10[:]=[]
    N10[:]=[]
#file3 for L=10 P=0.4
N4c=[]
S4c=[]
for i in range(1,1000):
    S10=[]
    N10=[]
    fileName="Dist_p 0.4 L 10 T {}".format(i)
    completeName = os.path.join(path, fileName+".txt")
    file= open(completeName,"r")
    lines=file.readlines()
    for x in lines:
        S10.append(x.split(' ')[0])
        N10.append(x.split(' ')[2])
    file.close()
    S10=S10[1:]
    S10=[float(item) for item in S10]
    N10=N10[1:]
    N10=[float(item) for item in N10]
    N4c=N4c+N10
    S4c=S4c+S10
    S10[:]=[]
    N10[:]=[]

#file4 for L=10 P=0.5
N5c=[]
S5c=[]
for i in range(1,1000):
    S10=[]
    N10=[]
    fileName="Dist_p 0.5 L 10 T {}".format(i)
    completeName = os.path.join(path, fileName+".txt")
    file= open(completeName,"r")
    lines=file.readlines()
    for x in lines:
        S10.append(x.split(' ')[0])
        N10.append(x.split(' ')[2])
    file.close()
    S10=S10[1:]
    S10=[float(item) for item in S10]
    N10=N10[1:]
    N10=[float(item) for item in N10]
    N5c=N5c+N10
    S5c=S5c+S10
    S10[:]=[]
    N10[:]=[]
    
    
#plt.loglog(x, y)

#PLOT   Distribution
plt.xlabel('S')
plt.ylabel('N(s,p,L')
plt.title('Distribution of clusters n(s, p,L)  for T=1000')
plt.plot(np.log(S2c),np.log(N2c),  'ro',label='p=0.2')
plt.plot(np.log(S3c),np.log(N3c), 'bs',label='p=0.3')
plt.plot(np.log(S4c),np.log(N4c),'g^', label='p=0.4')
plt.plot(np.log(S5c),np.log(N5c),'ys', label='p=0.5')
plt.legend()
plt.savefig('C:/Users/Gunel/Desktop/Percolation/Figures/Distribution.eps', format='eps')
plt.show()

