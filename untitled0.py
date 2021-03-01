import matplotlib.pyplot as plt
import csv
fileName1="Ave/Ave_L_10_T_10000.csv"
fileName2="Ave/Ave_L_50_T_10000.csv"
#file1
p=[]
sMax1=[]
sAve1=[]
dMin1=[]
Pflow1=[]
with open(fileName1, 'r') as f:

    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames

    for line in d_reader:
        p.append(line['p'])
        Pflow1.append(line['Pflow'])
        dMin1.append(line['dMin'])
        sMax1.append(line['Smax'])
        sAve1.append(line['Save'])  
f.close()
#file2
sMax5=[]
sAve5=[]
dMin5=[]
Pflow5=[]
with open(fileName2, 'r') as f:

    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames

    for line in d_reader:
        Pflow5.append(line['Pflow'])
        dMin5.append(line['dMin'])
        sMax5.append(line['Smax'])
        sAve5.append(line['Save'])  
f.close()

#PLOT1 Probability
plt.xlabel('p')
plt.ylabel('Pflow')
plt.title('Probability Pflow for T=1000')
plt.plot(p,Pflow1,  'ro-',label='L=10', linewidth=0.5)
plt.plot(p,Pflow5, 'bs-',label='L=50', linewidth=0.5)
plt.legend()
plt.savefig('Figures/Probability_Pflow_for.eps', format='eps')
plt.show()


#PLOT2 The average shortest path
plt.xlabel('p')
plt.ylabel('dmin')
plt.title('The average shortest path for T=1000')
plt.plot(p,dMin1, 'ro-',label='L=10', linewidth=0.5)
plt.plot(p,dMin5, 'bs-',label='L=50', linewidth=0.5)

plt.legend()
plt.savefig('Figures/Average_path.eps', format='eps')
plt.show()


#PLOT3 The average size of the maximum cluster
plt.xlabel('p')
plt.ylabel('Smax')
plt.title('The average size of the maximum cluster for T=1000')
plt.plot(p,sMax1, 'ro-',label='L=10', linewidth=0.5)
plt.plot(p,sMax5,  'bs-',label='L=50', linewidth=0.5)

plt.legend()
plt.savefig('Figures/AverageMax_cluster.eps', format='eps')
plt.show()

#PLOT4 The average size of the maximum cluster
plt.xlabel('p')
plt.ylabel('Save')
plt.title('The average size of the average cluster for T=1000')
plt.plot(p,sAve1,  'ro-',label='L=10', linewidth=0.5)
plt.plot(p,sAve5, 'bs-',label='L=50', linewidth=0.5)
plt.legend()
plt.savefig('Figures/AverageSize_average_cluster.eps', format='eps')
plt.show()

