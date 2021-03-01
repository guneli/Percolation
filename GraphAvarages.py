import matplotlib.pyplot as plt
import os.path
fileName1="Ave_L 10 T 1000"
fileName2="Ave_L 50 T 1000"
fileName3="Ave_L 100 T 1000"
path="C:/Users/Gunel/Desktop/Percolation/Average/"
completeName1 = os.path.join(path, fileName1+".txt")
completeName2 = os.path.join(path, fileName2+".txt")
completeName3 = os.path.join(path, fileName3+".txt")
#file1
file1= open(completeName1,"r")
lines=file1.readlines()
p=[]
sMax1=[]
sAve1=[]
dMin1=[]
Pflow1=[]
for x in lines:
    p.append(x.split(' ')[0])
    Pflow1.append(x.split(' ')[2])
    dMin1.append(x.split(' ')[4])
    sMax1.append(x.split(' ')[6])
    sAve1.append(x.split(' ')[9])  
file1.close()
p=p[1:]
p=[float(item) for item in p]
sMax1=sMax1[1:]
sMax1=[float(item) for item in sMax1]
sAve1=sAve1[1:]
sAve1=[float(item) for item in sAve1]
dMin1=dMin1[1:]
dMin1=[float(item) for item in dMin1]
Pflow1=Pflow1[1:]
Pflow1=[float(item) for item in Pflow1]
#file2
file2= open(completeName2,"r")
lines=file2.readlines()
sMax5=[]
sAve5=[]
dMin5=[]
Pflow5=[]
for x in lines:
    Pflow5.append(x.split(' ')[2])
    dMin5.append(x.split(' ')[4])
    sMax5.append(x.split(' ')[6])
    sAve5.append(x.split(' ')[9])  
file2.close()
sMax5=sMax5[1:]
sMax5=[float(item) for item in sMax5]
sAve5=sAve5[1:]
sAve5=[float(item) for item in sAve5]
dMin5=dMin5[1:]
dMin5=[float(item) for item in dMin5]
Pflow5=Pflow5[1:]
Pflow5=[float(item) for item in Pflow5]

#file3
file3= open(completeName3,"r")
lines=file3.readlines()
sMax10=[]
sAve10=[]
dMin10=[]
Pflow10=[]
for x in lines:
    Pflow10.append(x.split(' ')[2])
    dMin10.append(x.split(' ')[4])
    sMax10.append(x.split(' ')[6])
    sAve10.append(x.split(' ')[9])  
file3.close()
sMax10=sMax10[1:]
sMax10=[float(item) for item in sMax10]
sAve10=sAve10[1:]
sAve10=[float(item) for item in sAve10]
dMin10=dMin10[1:]
dMin10=[float(item) for item in dMin10]
Pflow10=Pflow10[1:]
Pflow10=[float(item) for item in Pflow10]
#PLOT1 Probability
plt.xlabel('p')
plt.ylabel('Pflow')
plt.title('Probability Pflow for T=1000')
plt.plot(p,Pflow1,  'ro-',label='L=10', linewidth=0.5)
plt.plot(p,Pflow5, 'bs-',label='L=50', linewidth=0.5)
plt.plot(p,Pflow10,'g^-', label='L=100', linewidth=0.5)
plt.legend()
plt.savefig('C:/Users/Gunel/Desktop/Percolation/Figures/Probability_Pflow_for.eps', format='eps')
plt.show()


#PLOT2 The average shortest path
plt.xlabel('p')
plt.ylabel('dmin')
plt.title('The average shortest path for T=1000')
plt.plot(p,dMin1, 'ro-',label='L=10', linewidth=0.5)
plt.plot(p,dMin5, 'bs-',label='L=50', linewidth=0.5)
plt.plot(p,dMin10,'g^-', label='L=100', linewidth=0.5)
plt.legend()
plt.savefig('C:/Users/Gunel/Desktop/Percolation/Figures/Average_path.eps', format='eps')
plt.show()


#PLOT3 The average size of the maximum cluster
plt.xlabel('p')
plt.ylabel('Smax')
plt.title('The average size of the maximum cluster for T=1000')
plt.plot(p,sMax1, 'ro-',label='L=10', linewidth=0.5)
plt.plot(p,sMax5,  'bs-',label='L=50', linewidth=0.5)
plt.plot(p,sMax10, p,'g^-', label='L=100', linewidth=0.5)
plt.legend()
plt.savefig('C:/Users/Gunel/Desktop/Percolation/Figures/AverageMax_cluster.eps', format='eps')
plt.show()

#PLOT4 The average size of the maximum cluster
plt.xlabel('p')
plt.ylabel('Save')
plt.title('The average size of the average cluster for T=1000')
plt.plot(p,sAve1,  'ro-',label='L=10', linewidth=0.5)
plt.plot(p,sAve5, 'bs-',label='L=50', linewidth=0.5)
plt.plot(p,sAve10,'g^-', label='L=100', linewidth=0.5)
plt.legend()
plt.savefig('C:/Users/Gunel/Desktop/Percolation/Figures/AverageSize_average_cluster.eps', format='eps')
plt.show()

