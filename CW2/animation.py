import matplotlib.pyplot as plt
from numpy import *
from pylab import *
import math
from matplotlib.animation import FuncAnimation

################# decie show animation of neuron iii spike moment ##########
iii = 2
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




tmidx = 0

# Scatter plot
fig = plt.figure(figsize = (10,6))
f1 = plt.scatter(positionx,positiony,marker = 'o', color ='grey',label = 'all visits',s = 5)
plt.title('Animation of rat moving around and spike moment of Neuron ' + str(iii))
plt.ylabel('y axis of the map')
plt.xlabel('x axis of the map')
axes = fig.add_subplot(111)
axes.set_xlim(min(positionx), max(positionx))
axes.set_ylim(min(positiony), max(positiony))

point, = axes.plot([positionx[0]],[positiony[0]], 'go')


def ani(coords):
	global tmidx
	tmidx = tmidx + 1
	print tmidx	
	if tmidx in names['timeindexN'+str(iii)]:
		print ('spike !!!!!!!!!spike!!!!!!!!!!!!!!!spike!!!!!!!!!!!!!!!')
		point.set_color('r')
	else:
		point.set_color('g')
	point.set_data([coords[0]],[coords[1]])
	point.set_label('rat position at moment ' + str(int(time[tmidx])))
	legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)
	return point

def frames():
    for x_pos, y_pos in zip(positionx, positiony):

        yield x_pos, y_pos

ani = FuncAnimation(fig, ani, frames=frames, interval=1)

legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)

plt.show()