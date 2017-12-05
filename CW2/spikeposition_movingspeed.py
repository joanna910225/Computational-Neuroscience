# coursework 2 q1
import matplotlib.pyplot as plt
from numpy import *
from pylab import *
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

# for loading x and y
f = open("x.csv")
positionx = map( lambda x: float(x.strip()), f.readlines() )
f = open("y.csv")
positiony = map( lambda x: float(x.strip()), f.readlines() )

# for loading time
f = open("time.csv")
time = map( lambda x: float(x.strip()), f.readlines() )

names = locals()
##plot positions in which each neuron fired

# Initializatoin
for n in range(1,5):
	names['timeindexN'+str(n)] = zeros(len(names['neuron'+str(n)]))
	names['xNeuron'+str(n)] = zeros(len(names['neuron'+str(n)]))
	names['yNeuron'+str(n)] = zeros(len(names['neuron'+str(n)]))


for n in range(1,5):
	names['timeindex'+str(n)] = 0
	for i, timespike in enumerate(names['neuron'+str(n)]):	
		out = 0
		while(out == 0):
			if timespike >= time[names['timeindex'+str(n)]] and timespike < time[names['timeindex'+str(n)] + 1]:
				out = 1
				lowerdiff = abs(timespike - time[names['timeindex'+str(n)]])
				upperdiff = abs(timespike - time[names['timeindex'+str(n)] + 1])
				if lowerdiff >= upperdiff:
					index = names['timeindex'+str(n)]
				else:
					index = names['timeindex'+str(n)]+1
			else:
				names['timeindex'+str(n)] = names['timeindex'+str(n)] + 1

		#print(index)
		names['timeindexN'+str(n)][i] = index
		names['xNeuron'+str(n)][i] = positionx[index]
		names['yNeuron'+str(n)][i] = positiony[index]


################## histogram of firing rate for each 1s interval #########
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

################# find large firing rate position for each neuron ############
def largeratepos(neuronx):
	activeposx = []
	activeposy = []
	hist,timex1,timex2 = firinghist(neuronx)
	threshold = 7
	j=0
	for i, t in enumerate(hist):
		if t >= threshold:
			while timex1[i] > time[j]:
				j=j+1
			#print j
			activeposx.append(positionx[j])
			activeposy.append(positiony[j])

	#for i,t in enumerate(activeposx):
		#print activeposx[i]
		#print activeposy[i]
	return activeposx,activeposy

############### find rat speed in one minute interval ########################
def speed():
	interval = 100000
	thresholdl = 3
	thresholds = 0.2
	speedlist = []
	largespeedx = []
	largespeedy = []
	smallspeedx = []
	smallspeedy = []
	beforeindex = 0
	for i, moment in enumerate(time):
		if moment - time[beforeindex] > interval:
			beforeindex = i
			distance = sqrt( (positionx[i-1] - positionx[beforeindex])**2 + (positiony[i-1] - positiony[beforeindex]) **2 )
			speedlist.append(distance)
			if distance >= thresholdl:
				largespeedx.append(positionx[i-1])
				largespeedy.append(positiony[i-1])
			elif distance < thresholds:
				smallspeedx.append(positionx[i-1])
				smallspeedy.append(positiony[i-1])


	print len(speedlist)
	print len(largespeedx)
	print len(smallspeedx)
	return speedlist,largespeedx,largespeedy,smallspeedx,smallspeedy



################# plot rat firing position for each neuron ############
fig = plt.figure(1)
plt.subplot(221)
f1 = plt.scatter(xNeuron1,yNeuron1,marker = '+', color = 'b', label = 'all fire positon', s = 5)
plt.title('Nueron 1 firing position')
plt.subplot(222)
f2 = plt.scatter(xNeuron2,yNeuron2,marker = '*', color = 'b', label = 'all fire positon', s = 5)
plt.title('Nueron 2 firing position')
plt.subplot(223)
f3 = plt.scatter(xNeuron3,yNeuron3,marker = 'x', color = 'b', label = 'all fire positon', s = 5)
plt.title('Nueron 3 firing position')
plt.subplot(224)
f4 = plt.scatter(xNeuron4,yNeuron4,marker = 'o', color = 'b', label = 'all fire position', s = 5)
plt.title('Nueron 4 firing position')

fig.suptitle('Position of the rat in which each neuron fired')
fig.subplots_adjust(hspace = 0.5)	




################## plot of large firing rate postion ##################

# figure(1)
# for i in range(1,5):
# 	subplot(2,2,i)
# 	activeposx,activeposy = largeratepos(names['neuron'+str(i)])
# 	plt.scatter(activeposx,activeposy,marker = 'o', color = 'r', label = 'Large firing rate position', s = 5)



################ plot of speed #####################################
figure(figsize = (10,5))
speedlist = []
speedlist,largespeedx,largespeedy,smallspeedx,smallspeedy = speed()
plt.plot(speedlist,)
ylabel("Speed (distance per sec)")
xlabel('Time (sec)')
title('Speed change in time')


################# plot of large speed position #################
# figure(1)
# for i in range(1,5):
# 	subplot(2,2,i)
# 	plt.scatter(largespeedx,largespeedy,marker = 'o', color = 'g', label = 'Large speed position', s = 5)


figure(1)
for i in range(1,5):
	subplot(2,2,i)
	plt.scatter(smallspeedx,smallspeedy,marker = 'o', color = 'c', label = 'Small speed position', s = 5)
 	legend(bbox_to_anchor=(0.0, 1), loc=2, borderaxespad=0.)

plt.show()

