# coursework 2 q4 histo
import matplotlib.pyplot as plt
from numpy import *
import math
# for loading neuron 1 - 4 and time
f = open("neuron1.csv")
neuron1 = map( lambda x: float(x.strip()), f.readlines() )
f = open("neuron2.csv")
neuron2 = map( lambda x: float(x.strip()), f.readlines() )
f = open("neuron3.csv")
neuron3 = map( lambda x: float(x.strip()), f.readlines() )
f = open("neuron4.csv")
neuron4 = map( lambda x: float(x.strip()), f.readlines() )

# for loading time
f = open("time.csv")
time = map( lambda x: float(x.strip()), f.readlines() )

# for loading x and y
f = open("x.csv")
positionx = map( lambda x: float(x.strip()), f.readlines() )
f = open("y.csv")
positiony = map( lambda x: float(x.strip()), f.readlines() )

def firinghist(neuronx):
	firenum = []
	firenum.append(0)
	timex1 = []
	interval = 10000
	count = 0
	max = time[0] + interval
	timex1.append(time[0])
	for i,t in enumerate(neuronx):
		while t >= max: 	
			timex1.append(max)		
			max = max + interval
			#print max
			#print count
			firenum.append(0)
			count = count + 1
		if t < max:
			firenum[count] = firenum[count] +1
	while max < time[-1]:
		timex1.append(max)	
		#print count
		#count = count + 1
		max = max + interval
		firenum.append(0)
	#firenum.append(0)

	timex2 = range(1,len(firenum)+1)
	#print time
	#print len(firenum)
	#print len(timex1)
	return firenum,timex1,timex2


########### plot firing rate for each 1 sec interval ################
names = locals()
fig1 = plt.figure(1)
for i in range (1,5):########
	hist,timex1,timex2 = firinghist(names['neuron'+str(i)])
	plt.subplot(4,1,i)
	plt.bar(timex1,hist,10000,color = 'black')
	#plt.plot(timex,hist,color = 'blue')
	plt.ylabel('firing rate (num/sec)')
	plt.xlabel('time sequence (sec/10000)')
	plt.grid(True)
	plt.title('Neuron '+ str(i))

fig1.suptitle('Firing Rates Histograms')
fig1.subplots_adjust(hspace = 1)

fig2 = plt.figure(2)
for i in range (1,5):########
	hist,timex1,timex2 = firinghist(names['neuron'+str(i)])
	plt.subplot(4,1,i)
	plt.bar(timex2,hist,1,color = 'black')
	#plt.plot(timex,hist,color = 'blue')
	plt.ylabel('firing rate (number/sec)')
	plt.xlabel('time sequence (sec)')
	plt.grid(True)
	plt.title('Neuron '+ str(i))
fig2.suptitle('Firing Rates Histograms')
fig2.subplots_adjust(hspace = 1)


########### large firing rate position #################
def largeratepos(neuronx):
	activeposx = []
	activeposy = []
	hist,timex1,timex2 = firinghist(neuronx)
	threshold = 10
	j=0
	for i, t in enumerate(hist):
		if t >= threshold:
			print t
			while timex1[i] < time[j]:
				j=j+1
			activeposx.append(positionx[j])
			activeposy.append(positiony[j])

	for i,t in enumerate(activeposx):
		print activeposx[i]
		print activeposy[i]
	return activeposx,activeposy



plt.show()

